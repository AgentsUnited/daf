import stomp
import os
from time import sleep
from amq_listener import AMQListener
import json
import traceback
import socket

INTERNAL_AMQ_HOST = os.getenv("INTERNAL_AMQ_HOST")
EXTERNAL_AMQ_HOST = os.getenv("EXTERNAL_AMQ_HOST")

def load_topics(type):
    with open("config.json", "r") as c:
        config = json.load(c)

    topics = []

    for mapping in config[type]:
        topics.append(mapping["from"])

    print(topics)

    return topics

def run():
    '''Runs the controller for the Dialogue and Argumentation Framework,
       listening for messages on the external ActiveMQ, and passing them on
       to the appropriate internal topic'''

    #connect to internal amq
    while True:

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((INTERNAL_AMQ_HOST, 61613))
            s.shutdown(2)
            break
        except:
            print("Waiting for ActiveMQ")
            sleep(3)

    while True:
        try:
            internal_conn = stomp.Connection([(INTERNAL_AMQ_HOST, 61613)])
            internal_conn.set_listener("AMQListener", AMQListener("internal"))
            internal_conn.start()
            internal_conn.connect()

            # internal amq subscribes to private topics in the outgoing array
            for topic in load_topics("outgoing"):
                internal_conn.subscribe(destination='/topic/' + topic, ack='auto', id=1)

            print("Connected to internal ActiveMQ")
            break
        except:
            print("Waiting for ActiveMQ")
            continue


    #connect to external activemq
    while True:
        try:
            external_conn = stomp.Connection([(EXTERNAL_AMQ_HOST, 61613)])
            external_conn.set_listener("AMQListener", AMQListener("external"))
            external_conn.start()
            external_conn.connect()

            for topic in load_topics("incoming"):
                print("Subscribing to: " + topic)
                external_conn.subscribe(destination='/topic/' + topic, ack='auto', id=1)

            print("Connected to external ActiveMQ")
            break
        except stomp.exception.ConnectFailedException:
            print("Waiting for external ActiveMQ")


    print("Dialogue and Argumentation Framework ready")
    while True:
        sleep(30)


if __name__ == '__main__':
    run()
