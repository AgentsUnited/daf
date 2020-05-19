import stomp
import json
import os

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

        if destination in self.topic_mapping:
            conn = stomp.Connection12([(self.amq_host, 61613)], auto_content_length=False)
            conn.start()
            conn.connect('admin','admin', wait=True)

            for d in self.topic_mapping[destination]:
                print("Destination: " + d)
                print("Message: " + body)
                conn.send(destination='/topic/' + d, body=body, header = {"ttl":30000})
