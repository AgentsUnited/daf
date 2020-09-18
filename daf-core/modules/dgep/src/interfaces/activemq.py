from dgep_interface import DGEPInterface
from threading import Thread
import stomp
import ast
import json
import dgep_endpoint

class ActiveMQ(DGEPInterface):
    """ Provides an ActiveMQ interface to and from DGEP
    """

    def __init__(self, amq_host='activemq-internal'):
        self.amq_host = amq_host
        self.conn = None

    def run(self, dgep):
        while True:
            try:
                self.conn = stomp.Connection([(self.amq_host, 61613)])
                self.conn.set_listener('DGEPListener', DGEPListener(self, self.conn, dgep))
                self.conn.start()
                self.conn.connect()
                self.conn.subscribe(destination='/topic/DGEP/requests', ack='auto', id=1)
                print("Connected to activemq")
                break
            except stomp.exception.ConnectFailedException:
                print("Waiting for ActiveMQ...")

    def disconnect(self):
        #print("Disconnect")
        self.conn.disconnect()


class DGEPListener(stomp.ConnectionListener):
    """ Provides the ActiveMQ listener to listen for commands
    """

    def __init__(self, amq_interface, conn, dgep, amq_host='activemq-internal'):
        self.conn = conn
        self.dgep = dgep
        self.amq_host = amq_host
        self.amq_interface = amq_interface

    def on_message(self, headers, body):
        """ Process a message received; messages are in the format:
                {"cmd":"<command>", "params"{"paramName":"paramValue"}}
            - cmd corresponds to a defined DGEP endpoint
            - params corresponds to the data required by that endpoint
        """
        data = json.loads(body)

        if "cmd" not in data.keys():
            self.send_message(json.dumps({"error":"no command specified"}))
        else:
            message = dgep_endpoint.invoke(self.dgep, data["cmd"], data["params"])
            # self.send_message(json.dumps(message), data["cmd"])
            self.send_message(json.dumps({"cmd": data["cmd"], "response": message}), data["cmd"])

    def send_message(self, message, cmd):
        """ Send a message to ActiveMQ
            DGEP will only send a message back, i.e. it will never initiate;
            thus, to ensure the message is sent to the correct topic, the command
            originally receieved is sent back

            :param message the message to send
            :param cmd the command originally sent to which this message is responding
            :type message json
            :type cmd str
        """

        if cmd == "moves" or cmd == "interaction" or cmd == "draftinteraction" or cmd == "commit":
            topic = "moves"
        else:
            topic = "response"

        print("Sending message:")
        print(message)

        conn = stomp.Connection12([(self.amq_host, 61613)], auto_content_length=False)
        conn.start()
        conn.connect('admin','admin', wait=True)
        conn.send(destination='/topic/DGEP/' + topic, body=message, headers = {"ttl": 30000})

    def disconnect(self):
        #print("Disconnecting from ActiveMQ")
        self.conn.disconnect()
        #print("ActiveMQ ended")
