import stomp
import time
import traceback
import json
import sys
import os
import threading
import logging
import socket
import uuid

amq_host = None

message_handlers = {}
command_handlers = {}
default_command_handlers = {}

options = {}

##
# set the log stuff
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
_logger.addHandler(handler)

def log(msg):
    _logger.info(msg)

def set_option(option, value):
    """
    Sets the given option with the given value
    Ensures that all option names are set to UPPERCASE
    """
    options[option.upper()] = value

def message_handler(topic, response_topic=None, respond=True):
    """
    Defines a decorator to define a class as a message handler
    By default anything returned by command handlers in the class will send to
    {topic}/response; this is overridden by providing a response_topic
    """

    if response_topic is None:
        response_topic = topic + "/response"

    if not respond:
        response_topic = None

    def wrapper(klass):
        message_handlers[topic] = {"handler": klass, "response_topic": response_topic}
        return klass
    return wrapper

def command_handler(command=None, response_topic=None, forward_topic=None, default=False):
    """
    Defines a decorator to define a class method as a command handler
    By default, anything returned is in the form of a "response" message; this is
    overridden by providing a forward_topic which will send on the output as a
    "request" message to the given topic
    A response topic can also be provided to override the default response topic
    for the message handler
    If a forward topic and response topic are both provided, and nether is None,
    the response topic is ignored
    """
    def wrapper(fn):

        if command is None and default == False:
            return fn

        handler_name = fn.__qualname__.split(".")[0]

        if command is not None:
            if handler_name not in command_handlers:
                command_handlers[handler_name] = {}

            command_handlers[handler_name][command] = {"fn": fn, "forward_topic": forward_topic, "response_topic": response_topic}

        if default:
            default_command_handlers[handler_name] = fn
            if handler_name not in command_handlers:
                command_handlers[handler_name] = {}

        return fn
    return wrapper

class Module(stomp.ConnectionListener):
    """
    Base class for a DAF module
    Provides the core functionality of connecting to ActiveMQ and handling
    messages
    """
    def __init__(self):
        self.amq_host = None
        self.name = "DAF-module"

    def handle_default(self, data):
        pass

    def on_message(self, headers, body):
        """
        Handle an incoming ActiveMQ message
        """

        try:
            destination = headers.get("destination", "").replace("/topic/","")

            log("Received message {} sent to {}".format(body, destination))

            if destination in message_handlers:
                response = None
                response_topic = None
                keyword = "response"

                handler = message_handlers.get(destination)

                if handler is not None:
                    response_topic = handler["response_topic"]

                    handler = handler["handler"]()
                    handler.destination = destination
                    handler.headers = headers

                    handler_class = handler.__class__.__name__

                    input = json.loads(body)
                    command = input.get("cmd",None)

                    if "params" not in input and "response" not in input:
                        params = {key: value for key,value in input.items() if key != "cmd"}
                        input["params"] = params

                    if command is not None:
                        command_handler = command_handlers.get(handler_class, {}).get(command, None)

                        if command_handler is not None:
                            data = input.get("params", input.get("response", {}))
                            response = command_handler["fn"](handler, command, data)

                            if command_handler["forward_topic"] is not None:
                                response_topic = command_handler["forward_topic"]
                                keyword = "params"
                            elif command_handler["response_topic"] is not None:
                                response_topic = command_handler["response_topic"]
                        else:
                            if handler_class in default_command_handlers:
                                response = default_command_handlers[handler_class](handler, command, input.get("params",input.get("response")))

                        if response is not None and response_topic is not None:
                            if options.get("RESPOND_WITH_COMMAND",True):
                                response = {"cmd": command, keyword: response}

                            response = json.dumps(response)
                            self.send_message(message=response, headers=headers, topic=response_topic)
        except:
            _logger.exception("Error")
            traceback.print_exc()

    def send_message(self, message, headers, topic):
        log("Sending message: {} to {}".format(message,topic))

        if "request-id" not in headers:
            headers["request-id"] = uuid.uuid4()

        log("RequestID: {}".format(headers["request-id"]))

        headers["ttl"] = 30000

        conn = stomp.Connection12([self.amq_host], auto_content_length=False)
        conn.connect('admin', 'admin', wait=True)
        conn.send(destination='/topic/' + topic, body=message, headers=headers)
        conn.disconnect()

    def run(self, name="DAF-module", host=('activemq-internal', 61613), thread=False):
        """
        Runs this module on the given activeMQ host
        """

        self.name = name
        # inner function for looping: required for threading
        def loop():
            while True:
                time.sleep(30)

        self.amq_host = host

        # supress connection errors from displaying on the console
        old_stderr = sys.stderr;
        f = open(os.devnull, 'w')
        sys.stderr = f


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tries = 0

        while True or tries > 4:
            result = s.connect_ex(host)

            if result == 0:
                break
            else:
                log("Waiting for ActiveMQ to come up")
                tries = tries + 1
                time.sleep(3)

        try:
            conn = stomp.Connection12([host])
            conn.set_listener('DAFModuleListener', self)
            conn.connect()

            i = 1
            for topic in message_handlers:
                log("Subscribing to: " + "/topic/" + topic)
                conn.subscribe(destination="/topic/" + topic, ack="auto", id=i)
                i = i + 1

            if thread:
                t = threading.Thread(target=loop)
                t.start()
            else: # just call the loop function in blocking mode
                loop()

        except stomp.exception.ConnectFailedException:
            _logger.error("Error connecting to ActiveMQ")
        except ConnectionRefusedError:
            _logger.error("Error connecting to ActiveMQ")

        log("Connected")

        # put stderr back
        sys.stderr = old_stderr
