import json
import daf
import mongo
from handlers import *

def check_first_run():
    if not mongo.ready():

        print("Executing first run script...")
        file = "firstrun/{file}.json"

        db = mongo.get_db()

        collections = ["argument_models", "dictionary", "content_descriptors", "variables"]

        for c in collections:
            with open(file.replace("{file}",c), "r") as f:
                f = json.load(f)
                db[c].insert_one(f)

if __name__ == '__main__':
    check_first_run()
    daf.Module().run(host=('activemq-internal',61613))
