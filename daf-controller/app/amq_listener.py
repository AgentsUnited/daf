import stomp
import json
import os
import uuid

_dialogue_topic_map = {
    "goalsetting": "UG",
    "introduction": "WOOL",
    "agenttest": "UG",
    "goalsetting1": "WOOL",
    "gatherinformation":"WOOL"
}

_wool_start_id = 10000

_wool_dialogue_ids = []

class AMQListener(stomp.ConnectionListener):
    '''Class to listen for ActiveMQ internal or external ActiveMQ messages and
       pass them off, respectively, to the external or internal ActiveMQ'''

    def __init__(self, type):
        ''' Constructor
            :param type the type of listener (internal or external)
            :type type str'''

        self.type = type

        if self.type == "external":
            self.amq_host = os.getenv("INTERNAL_AMQ_HOST")
        elif self.type == "internal":
            self.amq_host = os.getenv("EXTERNAL_AMQ_HOST")

        self.topic_mapping = {}

        self.load_config()

    def load_config(self):
        ''' Load the configuration from the JSON file to determine the mapping
            from external to internal ActiveMQ topics'''

        with open("config.json", "r") as c:
            self.config = json.load(c)

        '''if we're listening to external amq we want incoming mappings;
           if we're listening to internal amq we want outgoing mappings'''
        if self.type == "external":
            m = "incoming"
        elif self.type == "internal":
            m = "outgoing"

        for mapping in self.config[m]:
            self.topic_mapping[mapping["from"]] = mapping["to"]

    def on_message(self, headers, body):
        ''' React to an incoming message, passing it on if a mapping exists
            to do so'''

        #trim off the /topic/ from the start of the destination
        destination = headers["destination"][7:]

        message = json.loads(body)

        cmd = message.get("cmd", None)

        tmp = None

        if "response" in message:
            message = message["response"]
        else:
            if "params" not in message and cmd is not None:
                params = {}

                for k,v in message.items():
                    if k != "cmd":
                        params[k] = v
                message["params"] = params

        if destination in self.topic_mapping:
            if destination == "DGEP/requests":
                params = message.get("params",{})

                if cmd == "new":
                    topic = params.get("topic","").lower()
                    d = _dialogue_topic_map.get(topic, None)

                    if d is not None:

                        tmp = [d + "/requests"]
                        if d == "WOOL":
                            dialogueID = _wool_start_id + len(_wool_dialogue_ids)
                            _wool_dialogue_ids.append(dialogueID)
                            message["params"]["dialogueID"] = dialogueID
                else:
                    dialogueID = params.get("dialogueID",None)

                    if dialogueID is not None and dialogueID in _wool_dialogue_ids:
                        tmp = ["WOOL/requests"]

            if tmp is None:
                tmp = self.topic_mapping[destination]

        # if tmp is still none, we can't do anything...
        if tmp is None:
            return

        body = json.dumps(message)

        conn = stomp.Connection12([(self.amq_host, 61613)], auto_content_length=False)
        conn.start()
        conn.connect('admin','admin', wait=True)

        for d in tmp:
            print("Destination: " + d)
            print("Message: " + body)
            conn.send(destination='/topic/' + d, body=body, header = {"ttl":30000})

        conn.disconnect()
