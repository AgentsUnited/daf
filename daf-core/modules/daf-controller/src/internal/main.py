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
    dir = "/demo"

    mongo.drop_db() # clears the demo db; mongo module has a check such that only the demo db can be dropped
    db = mongo.get_db()

    for file in os.listdir(dir):
        if file.endswith(".json"):
            collection = file[:-5]
            with open(dir + "/" + file, "r") as f:
                f = json.load(f)

                if type(f) is list:
                    for r in f:
                        db[collection].insert_one(r)
                else:
                    db[collection].insert_one(f)

def init():
    # the internal listener is a little different; we can't decorate the handler class
    # because we only know the available platforms at runtime. So we do it manually,
    # directly accessing the daf decorator functions

    col = mongo.get_column("dialogue_topics")
    result = col.find({})

    if result:
        for r in result:
            if "platform" in r:
                destination = r["platform"] + "/response"
                daf.message_handler(destination, respond=False)(ResponseHandler)()
                destination = r["platform"] + "/dialogue_moves"
                daf.message_handler(destination, respond=False)(ResponseHandler)()

if __name__ == '__main__':
    if os.getenv("DEMO","False") == "True":
        demo()
    external.host=('activemq-external',61613)  # for sending to external
    init()
    daf.Module().run(host=('activemq-internal',61613))
