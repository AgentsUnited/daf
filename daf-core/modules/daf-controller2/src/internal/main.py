import json
import os
from daf import mongo
import daf
import activemq as external
from .handlers import *

def demo():
    """
    Function to load in the demo content
    """
    print("Executing DEMO script...")
    file = "/demo/{file}.json"

    mongo.drop_db() # clears the demo db; mongo module has a check such that only the demo db can be dropped

    db = mongo.get_db()

    collections = ["argument_models", "dictionary", "content_descriptors", "variables", "dialogue_topics"]

    for c in collections:
        with open(file.replace("{file}",c), "r") as f:
            f = json.load(f)

            if type(f) is list:
                for r in f:
                    db[c].insert_one(r)
            else:
                db[c].insert_one(f)

    db["dialogues"].insert_one({}) # creates dialogues collection


def init():
    # the internal listener is a little different; we can't decorate the handler class
    # because we only know the available platforms at runtime. So we do it manually,
    # directly accessing the daf decorator functions

    col = mongo.get_column("dialogue_topics")
    result = col.find({})

    if result:
        print("Result from")
        for r in result:
            if "platform" in r:
                destination = r["platform"] + "/response"
                print("Subscribing to " + destination)
                daf.message_handler(destination, respond=False)(ResponseHandler)()
                destination = r["platform"] + "/dialogue_moves"
                daf.message_handler(destination, respond=False)(ResponseHandler)()

if __name__ == '__main__':
    if os.getenv("DEMO","False") == "True":
        demo()
    external.host=('activemq-external',61613)  # for sending to external
    init()
    daf.Module().run(host=('activemq-internal',61613))
