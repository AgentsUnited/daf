import os
import json
import daf
from daf import mongo
import activemq as internal
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


# we only want to send data back with responses; don't include the command
daf.set_option("RESPOND_WITH_COMMAND", False)

if __name__ == '__main__':
    if os.getenv("DEMO","False") == "True":
        demo()

    internal.host=('activemq-internal',61613)  # for sending to internal
    daf.Module().run(host=('activemq-external',61613))
