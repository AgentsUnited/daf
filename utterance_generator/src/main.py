import stomp
import time
import ast
import json
import sys
import os
from utterance_generator import UtteranceGenerator
import traceback
import pymongo
import hashlib
import datetime

handlers = {}

def handler(input, output=None):

    def wrapper(fn):
        handlers["/topic/" + input] = {"input": fn, "output": output}
        return fn

    return wrapper

class UtteranceGeneratorListener(stomp.ConnectionListener):
    """ Provides the ActiveMQ listener to listen for commands
    """

    def __init__(self):
        self.amq_host = 'activemq-internal'

        self.auth_token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJtLnNuYWl0aEBkdW5kZWUuYWMudWsiLCJpYXQiOjE1NzEyOTk0NDIsImV4cCI6MTU3MTM4NTg0MiwiaGFzaCI6InpmRFZIcU95UDBqNFdRQlFzUytDbjNCbjgzNFd5VC9vRjlzMzNuSE9sTVE9In0.3EvKURPwzwfZCPpPD-j9Y-bg8W4HcEwxwzGjHIaGyW05qrg8zQOHE6rS6k3O3GnIJ-jbVNS_Qh0-BVYR2Abvgw"

        self.dialogues = {}


        self.content_models = {
            "argument_rules":{
                "protocol": None,
                "preferences": [],
                "contrariness": [],
                "rules": [],
                "premises": []
            },
            "dictionary":{
                "protocol": None,
                "language": "EN",
                "entries": {}
            },
            "variables":{
                "protocol": None,
                "variables": {}
            },
            "content_descriptors":{
                "protocol": None,
                "descriptors": {}
            }
        }


    def generate_session_id(self, data):
        hash_string = str(data) + str(datetime.datetime.now())
        return hashlib.md5(hash_string.encode('utf-8')).hexdigest()

    def new_dialogue(self, data):
        #self.auth_token = data["authToken"]
        # create a session id to temporarily tie together requests until we have a dialogue ID
        session_id = self.generate_session_id(data)

        if "filstantiator" in data.keys():
            self.add_coaches(data["filstantiator"].copy(), session_id);
        elif "utteranceParams" in data.keys():
            self.add_coaches(data["utteranceParams"].copy(), session_id)

        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["users"]


        col.update_one({"username": data["username"]}, {"$set":{"dialogueID": session_id}})

        return session_id

    def set_dialogue_id(self, session_id, dialogue_id):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["coach_specifications"]

        filter = {"sessionID": session_id}

        col.update_many(filter, {"$set" : {"dialogueID": dialogue_id}})

        col = db["users"]
        col.update_one({"dialogueID": session_id}, {"$set":{"dialogueID": dialogue_id}})

        # update the stored protocol
        protocol = self.dialogues[session_id]
        self.dialogues[dialogue_id] = protocol
        del self.dialogues[session_id]

    def add_coaches(self, data, session_id):

        print("Adding coaches")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        database = os.getenv("MONGODB")
        db = mongo[database]
        coaches = db["coach_specifications"]

        # this will need updated when the new content selection algorithm is implemented
        if type(data) is list:
            coaches_data = {}
            for c in data:
                tmp = {}
                name = None

                if "participant" in c:
                    name = c["participant"]

                if "move_style_preferences" in c["parameters"]:
                    m = c["parameters"]["move_style_preferences"].split("<")
                    tmp["personality"] = m[len(m) - 1].strip()

                coaches_data[name] = tmp


            data = coaches_data

        to_add = {
            "sessionID": session_id,
            "coaches": data
        }

        coaches.insert_one(to_add)

    def store_moves(self, moves, dialogueID):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["move_cache"]

        to_store = {"moves": moves, "dialogueID": dialogueID}

        col.insert_one(to_store)

    def clear_move_cache(self, dialogueID):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["move_cache"]

        col.delete_one({"dialogueID": dialogueID})

    def get_cached_moves(self, dialogueID):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["move_cache"]

        result = col.find_one({"dialogueID": dialogueID})

        if result is not None and "moves" in result:
            return result["moves"]

        return None

    @handler("FILSTANTIATOR/auth")
    def handle_auth(self, data):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["users"]

        if "cmd" in data:
            if data["cmd"] == "login":
                result = col.find_one({"username": data["username"]})

                if result is None:
                    col.insert_one(data)
                else:
                    col.update({'username': data["username"]}, {"$set" : {"authToken": data["authToken"]}})
            elif data["cmd"] == "logout":
                result = col.find_one({"username": data["username"]})

                if result:
                    dialogueID = result["dialogueID"]

                    col.delete_one({'username': data["username"]})
                    col = db["move_cache"]
                    col.delete_one({'dialogueID': dialogueID})

    @handler("FILSTANTIATOR/requests", "DGEP/requests")
    def handle_request(self, data):
        if data["cmd"] == "new":
            if "params" in data.keys():
                session_id = self.new_dialogue(data["params"])
                print("Session ID: " + str(session_id))
                data["params"]["sessionID"] = session_id
                if data["params"]["topic"] == "GOALSETTING":
                    data["params"]["topic"] = "GoalSetting"
                self.dialogues[session_id] = data["params"]["topic"]
                data["params"]["protocol"] = data["params"]["topic"]

                print("Sending data to DGEP: " + str(data))

        elif data["cmd"] == "interaction" or data["cmd"] == "draftinteraction":
            if "params" in data.keys():
                params = data["params"]
                dialogueID = params["dialogueID"]
                self.clear_move_cache(dialogueID)
                if "reply" in params.keys():
                    reply = params["reply"]
                    for r in reply.keys():
                        content = reply[r]
        elif data["cmd"] == "moves" or data["cmd"] == "commit":
            pass
        else:
            data["params"]["sessionID"] = self.generate_session_id(data)

        return data

    @handler("DGEP/moves", "FILSTANTIATOR/dialogue_moves")
    def handle_moves(self, data):
        dialogueID = data["dialogueID"]
        topic = "FILSTANTIATOR/dialogue_moves"

        moves = self.get_cached_moves(dialogueID)

        if moves is not None:
            data["moves"]  = moves
        else:
            if "moves" in data:
                data["moves"] = UtteranceGenerator(self.dialogues[dialogueID], dialogueID).process_moves(data["moves"])
            else:
                data["moves"] = {}

            self.store_moves(data["moves"], dialogueID)

        return data

    @handler("DGEP/response", "FILSTANTIATOR/response")
    def handle_response(self, data):
        if "dialogueID" in data.keys() and "sessionID" in data.keys():
            sessionID = data["sessionID"]
            dialogueID = data["dialogueID"]

            print("Setting dialogue ID " + str(dialogueID) + " for sessionID " + sessionID)

            self.set_dialogue_id(sessionID, dialogueID)

            tmp = data["moves"]
            tmp["dialogueID"] = data["dialogueID"]
            instantiated_moves = UtteranceGenerator(self.dialogues[dialogueID],dialogueID).process_moves(tmp)
            data["moves"] = instantiated_moves

            self.store_moves(instantiated_moves, dialogueID)

            data["clearvars"] = self.get_clear_vars(dialogueID)

            print("Returning data")
            print(str(data))
        elif "protocol" in data.keys():
            self.initialise_content(data["protocol"])

        return data


    def initialise_content(self, protocol):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]

        protocol = protocol.lower();

        for key, value in self.content_models.items():
            col = db[key];

            result = col.find_one({"protocol": protocol})

            if result is None:
                value["protocol"] = protocol
                col.insert_one(value);

    def get_clear_vars(self, dialogueID):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["variables"]

        to_return = []

        result = col.find_one({"protocol": self.dialogues[dialogueID]})

        if "variables" in result:
            for move_name, variables in result["variables"].items():
                for name,params in variables.items():
                    if "clear_on_new" in params:
                        if params["clear_on_new"] == True:
                            to_return.append(name)

        return to_return

    def on_message(self, headers, body):

        try:
            destination = headers["destination"]
            input_data = ast.literal_eval(body)
            if destination in handlers:
                handler = handlers[destination]

                output_data = handler["input"](self, input_data)

                if handler["output"] is not None and output_data is not None:
                    self.send_message(json.dumps(output_data), handler["output"])
        except Exception as e:
            print("Error in utterance generator")
            traceback.print_exc()

    def send_message(self, message, topic="FILSTANTIATOR/dialogue_moves"):

        print("UtteranceGenerator sending to " + topic + ":")

        conn = stomp.Connection12([(self.amq_host, 61613)], auto_content_length=False)
        conn.start()
        conn.connect('admin','admin', wait=True)
        conn.send(destination='/topic/' + topic, body=message, headers = {"ttl": 30000})


def check_first_run():

    db_name = "couch_content"

    mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
    file = "assets/firstrun/{file}.json"

    if db_name not in mongo.list_database_names():

        print("Executing first run script...")

        db = mongo[db_name]

        coach_specifications = db["coach_specifications"]
        dictionary = db["dictionary"]
        argument_rules = db["argument_rules"]
        vars = db["variables"]
        content_descriptors = db["content_descriptors"]
        coaching_variables = db["coaching_variables"] # for testing - should normally interface with skb

        with open(file.replace("{file}","dictionary"), "r") as d:
            d = json.load(d)

            for p in d:
                dictionary.insert_one(p)

        with open(file.replace("{file}", "argument_rules"), "r") as rules:
            rules = json.load(rules)

            for protocol in rules:
                argument_rules.insert_one(protocol)

        with open(file.replace("{file}", "variables"), "r") as variables:
            variables = json.load(variables)

            for v in variables:
                vars.insert_one(v)

        with open(file.replace("{file}", "content_descriptors"), "r") as cd:
            cd = json.load(cd)

            for c in cd:
                content_descriptors.insert_one(c);

        with open(file.replace("{file}", "coaching_variables"), "r") as cv:
            cv = json.load(cv)

            coaching_variables.insert_one(cv);


if __name__ == '__main__':
    check_first_run()
    #supress connection errors from displaying on the console
    old_stderr = sys.stderr;
    f = open(os.devnull, 'w')
    sys.stderr = f
    while True:
        try:
            conn = stomp.Connection([('activemq-internal', 61613)])
            conn.set_listener('UtteranceGeneratorListener', UtteranceGeneratorListener())
            conn.start()
            conn.connect()
            #listen in on the requests topic to get the requests stuff
            conn.subscribe(destination='/topic/FILSTANTIATOR/requests', ack='auto', id=1)
            conn.subscribe(destination='/topic/FILSTANTIATOR/auth', ack='auto', id=1)
            conn.subscribe(destination='/topic/DGEP/moves', ack='auto', id=1)
            conn.subscribe(destination='/topic/DGEP/response', ack='auto', id=1)
            print("Connected to ActiveMQ")
            print("UtteranceGenerator started")
            break
        except stomp.exception.ConnectFailedException:
            print("Waiting for ActiveMQ...")
        except ConnectionRefusedError:
            print("Waiting for ActiveMQ...")

    # put stderr back
    sys.stderr = old_stderr

    #keep alive
    while True:
        time.sleep(30)
