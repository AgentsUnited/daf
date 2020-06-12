import ast
from .defcon.system import System
import os
import traceback
import stomp
import pickle
import re
from .dgdl.dgdl_file import dgdl_file
from .dgdl.factories.system_factory import SystemFactory
from .defcon.dialogue_manager import DialogueManager
from dgdl.yarn.yarn import Yarn
from interfaces.dgep_endpoint import *
from interfaces.dgep_interface import DGEPInterface
from threading import Thread
import copy

class DGEP(DialogueManager):

    def __init__(self):

        self.interfaces = []

        self.dialogues = []
        self.loaded_plugins = {}

        self.amq = None
        self.rest = None
        self.amq_active = False

        self.draft_interaction_data = {}

        ''' Load saved dialogues '''
        dialogues_path = os.path.dirname(os.path.realpath(__file__)) + "/dialogues"

        ''' Create the dialogues dir if it doesn't exist '''
        if not os.path.exists(dialogues_path):
            os.mkdir(dialogues_path)

        for f in os.listdir(dialogues_path):
            id = f.split('.')[0]
            p = pickle.load(open(dialogues_path + "/" + f, 'rb'))
            p.dgep = self
            self.dialogues.insert(int(id), p)

    def add_interface(self, interface):
        if isinstance(interface, DGEPInterface):
            self.interfaces.append(interface)

    def run(self):
        threads = []
        count = 0
        for i in self.interfaces:
            threads.append(Thread(target=i.run, args=[self]))
            threads[count].start()
            count = count + 1

    @dgep_endpoint('new')
    def new_dialogue(self, data, system=None):
        try:
            '''If this is a sub-dialogue of an existing dialogue, we should already have a protocol'''
            if system is not None:
                protocol = data["protocol"]
                data = system.data
                data["protocol"] = protocol

            to_return = {}
            if "protocol" in list(data.keys()):
                protocol = data["protocol"]

                ''' If the provided protocol starts yarn. translate it first'''
                if protocol[:5] == 'yarn.':
                    if "username" in list(data.keys()):
                        protocol = Yarn().convert_to_dgdl(protocol[5:], data["username"])
                    else:
                        protocol = Yarn().convert_to_dgdl(protocol[5:])

                s = SystemFactory(self).get_system(protocol)

                if "participants" in list(data.keys()):
                    to_return["participants"] = []
                    participants = data["participants"]
                    for p in participants:
                        if "player" in list(p.keys()):
                            if "name" in list(p.keys()):
                                participantID = s.add_participant(p["player"], p["name"])
                                to_return["participants"].append({"participantID": participantID, "name":p["name"]})
                            else:
                                participantID = s.add_participant(p["player"])
                                to_return["participants"].append({"participantID": participantID})

                if not s.start():
                    return {"error": s.last_error, "source":"system"}

                self.dialogues.append(s)
                dialogueID = len(self.dialogues)

                p = os.path.dirname(os.path.realpath(__file__)) + "/dialogues/" + str(dialogueID) + ".dialogue"
                pickle.dump(s, open(p, "w+"), protocol=2)

                to_return["dialogueID"] = len(self.dialogues)
                to_return["moves"] = s.get_available_moves()

                return to_return
            else:
                return {"error": "no protocol specified", "source":"dgep"}
        except Exception as e:
                traceback.print_exc()
                return {"error": str(e), "source":"dgep"}

    @dgep_endpoint('dialogues')
    def get_dialogues(self, data):
        dialogues = []

        dialogues_path = os.path.dirname(os.path.realpath(__file__)) + "/dialogues"
        for f in os.listdir(dialogues_path):
            id = f.split('.')[0]
            p = pickle.load(open(dialogues_path + "/" + f, 'rb'))

            dialogues.append({"id": id, "protocol": p.name})

        return {"dialogues": dialogues}

    def end_dialogue(self, data):
        id = data["id"]
        dialogues_path = os.path.dirname(os.path.realpath(__file__)) + "/dialogues"
        os.remove(dialogues_path + "/" + id + ".dialogue")

    @dgep_endpoint('join', ['dialogueID'])
    def join_dialogue(self, data):
        dialogueID = int(data["dialogueID"])

        if dialogueID < len(self.dialogues):
            system = self.dialogues[dialogueID]
            return {"dialogueID": dialogueID, "protocol": system.name}
        else:
            return {"error":"No such dialogue"}

    @dgep_endpoint('test')
    def test_dgep(self, data):
        return {"message": "OK", "input_data": data}

    @dgep_endpoint('moves', ['dialogueID'])
    def dialogue_moves(self, data):
        dialogueID = int(data["dialogueID"])

        if self.dialogues[dialogueID - 1]:
            dialogue = self.dialogues[dialogueID - 1]

            if dialogue.terminated:
                status = "terminated"
            else:
                status = "active"

            moves = {"dialogueID": dialogueID,
                     "moves": dialogue.get_available_moves(),
                     "status": status
                     }

            #m = dialogue.get_available_moves()
            #m["dialogueID"] = dialogueID

            return moves
        else:
            return {"error":"Dialogue not found"}

    @dgep_endpoint('interaction')
    def dialogue_interaction(self, data):
        '''TODO:
            1) check for draft data; delete if exists
        '''
        dialogueID = data["dialogueID"]

        if self.dialogues[dialogueID-1]:
            dialogue = self.dialogues[dialogueID - 1]

            interaction_id = data["moveID"]

            if "reply" in data["reply"]:
                d = data["reply"]
            else:
                d = {"reply": data["reply"]}

            interaction_data = {"speaker": data["speaker"],
                                "target": data["target"],
                                "content": d}

            print("data: " + str(data))
            print("interaction data: " + str(interaction_data))


            effects = dialogue.perform_interaction(interaction_id, interaction_data)

            p = os.path.dirname(os.path.realpath(__file__)) + "/dialogues/" + str(dialogueID) + ".dialogue"
            pickle.dump(dialogue, open(p, "w+"), protocol=2)

            print("Returning effects:" + str(effects))

            if dialogue.terminated:
                status = "terminated"
            else:
                status = "active"

            effects = {"dialogueID": dialogueID, "status": status, "moves": effects}

            #if dialogue.terminated:
            #    effects = {"dialogueID": dialogueID, "vars": dialogue.runtime_vars}

            return effects
        else:
            return {"Error":"Dialogue not found"}

    @dgep_endpoint('draftinteraction')
    def draft_dialogue_interaction(self, data):
        '''TODO:
            1) Deep copy of dialogue object
            2) Build interaction_data structures etc. as above
            3) Store interaction data for future commit (overwrite previous)
            4) Perform the interaction on the deep copy
        '''

        dialogueID = data["dialogueID"]

        if self.dialogues[dialogueID - 1]:
            # deep copy of the dialogue so that changes don't (yet) persist
            dialogue = copy.deepcopy(self.dialogues[dialogueID - 1])

            interaction_id = data["moveID"]

            if "reply" in data["reply"]:
                d = data["reply"]
            else:
                d = {"reply": data["reply"]}

            interaction_data = {"speaker": data["speaker"],
                                "target": data["target"],
                                "content": d}

            self.draft_interaction_data[dialogueID] = {"interaction_id": interaction_id, "interaction_data": interaction_data}

            effects = dialogue.perform_interaction(interaction_id, interaction_data)

            if dialogue.terminated:
                status = "terminated"
            else:
                status = "active"

            effects = {"dialogueID": dialogueID, "status": status, "moves": effects}

            return effects
        else:
            return {"Error": "dialogue not found"}

    @dgep_endpoint('commit')
    def commit_dialogue_interaction(self, data):
        ''' TODO:
            1) Check for draft interaction data; error out if not
            2) Perform interaction data on actual dialogue object
            3) Clean up draft data
        '''

        dialogueID = data["dialogueID"]

        if dialogueID not in self.draft_interaction_data:
            return {"Error":"No draft interaction found for dialogue ID " + str(dialogueID)}

        interaction_data = self.draft_interaction_data[dialogueID]

        if self.dialogues[dialogueID - 1]:
            dialogue = self.dialogues[dialogueID - 1]

            effects = dialogue.perform_interaction(interaction_data["interaction_id"], interaction_data["interaction_data"])

            p = os.path.dirname(os.path.realpath(__file__)) + "/dialogues/" + str(dialogueID) + ".dialogue"
            pickle.dump(dialogue, open(p, "w+"), protocol=2)

            print("Returning effects:" + str(effects))

            if dialogue.terminated:
                status = "terminated"
            else:
                status = "active"

            effects = {"dialogueID": dialogueID, "status": status, "moves": effects}

            return effects
        else:
            return {"Error": "dialogue not found"}

    @dgep_endpoint('protocol', ['name'])
    def get_protocol(self, data):

        protocol = data["name"]

        if "action" in data.keys():
            if data["action"] == "test":
                d = dgdl_file()
                t = d.test(protocol)
                return {"output": t}
            elif data["action"] == "save":
                dgdl = data["protocol"]
                f = dgdl_file().create(protocol, dgdl)

                test = dgdl_file().test(protocol).strip();

                if test == "":
                    test = []
                else:
                    test = test.split("\n")

                return {"status":"OK", "test": test}

        if protocol + ".dgdl" in os.listdir("src/assets/protocols"):
            file = open("src/assets/protocols/" + protocol + ".dgdl")
            output = file.read()
            file.close()
            return {protocol: output}
        else:
            return {"error":"protocol not found"}

    @dgep_endpoint('protocols')
    def get_protocols(self, data):
        protocols = []
        for f in os.listdir("src/assets/protocols"):
            if f.endswith(".dgdl"):
                protocol = open("src/assets/protocols/" + f).read()

                regex = r"(?<=Description:)(.*)(?=\*\/)"
                matches = re.finditer(regex, protocol, re.MULTILINE)

                description = ""
                for matchNum, match in enumerate(matches, start=1):
                    description = match.group()

                regex = r"player{(.*)}"
                matches = re.finditer(regex, protocol, re.MULTILINE)

                players = []

                for matchNum, match in enumerate(matches, start=1):
                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1
                        player_spec = match.group(groupNum).split(",")

                        player_id = player_spec[0].split(":")[1].strip()

                        max_players = ""
                        min_players = ""

                        for i in range(1,len(player_spec)):
                            if player_spec[i].strip().startswith("max"):
                                max_players = int(player_spec[i].split(":")[1])
                            elif player_spec[i].strip().startswith("min"):
                                min_players = int(player_spec[i].split(":")[1])

                        players.append({"id":player_id, "max":max_players,"min":min_players})

                protocols.append({"name":f[:-5], "description":description, "players":players})

        return {"protocols":protocols}

    @dgep_endpoint('plugins')
    def get_plugins(self, data):
        return {"plugins": os.walk('src/plugin').next()[1]}


    @dgep_endpoint('plugin', ['name'])
    def get_plugin(self, data):
        manifest = {}
        plugin_name = data["name"]

        with open('src/plugin/' + plugin_name + '/MANIFEST') as file:
            line = file.readline()

            while line:
                v = line.split("=")
                manifest[v[0]] = v[1]
                line = file.readline()

        edit_template = open('src/plugin/' + plugin_name + '/config/template.htm').read()
        manifest["template"] = edit_template

        return {"plugin": manifest}

    @dgep_endpoint('yarn')
    def translate_yarn(self, data):
        if "yarnfile" in data.keys():
            return {"dgdl_file":Yarn().convert_to_dgdl(data["yarnfile"])}
        else:
            return {"error":"No Yarn file provided"}
