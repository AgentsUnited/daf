import pymongo
import re
from content.descriptors import *
import os

class UtteranceGenerator:

    """
    Class that encapsulates the high-level functionality for generating
    utterances

    The process of finding actual content is handed over to descriptors that
    process the .rules files that define how content should be found for specific
    move types.

    Attributes:
        protocol (str): the protocol that is being followed
    """

    def __init__(self, protocol, dialogueID):

        #self.descriptors_new = ContentDescriptorLoader('assets/' + protocol + '.rules').get_descriptors()
        self.descriptors_new = ContentDescriptorLoader(protocol).get_descriptors()
        self.protocol = protocol

        self.dialogueID = dialogueID

        self.descriptor_handlers = {
            "aspic": ArgumentDescriptor,
            "input": InputDescriptor
        }

        self.value_regex = re.compile(r"(?:[^() ])+\(([^()]+)\)")

    def get_move_styles(self):
        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["coach_specifications"]

        result = col.find_one({"dialogueID": self.dialogueID})

        to_return = {}

        if "coaches" in result.keys():
            for coach, personality in result["coaches"].items():
                to_return[coach] = personality["personality"]

        return to_return

    def process_moves(self, moves, agent_specifications=None):

        to_return = {}

        possible_content = self.select_move_content(moves)

        dialogueID = self.dialogueID

        for participant, moves in moves.items():
            if participant not in possible_content:
                continue

            to_return[participant] = []

            for moveName,content in possible_content[participant].items():
                content = self.filter_content(participant, moveName, content) # TODO

                if content:
                    for c in content:
                        variables = self.get_variables(moveName, c["reply"])
                        to_return[participant].append({"moveID": moveName, "reply": c["reply"], "opener": c["opener"],"target": c["target"], "vars": variables})

        return to_return


    def get_variables(self, moveName, reply):
        """ Method to map replies to variables the content should be stored in
            in the SKB """

        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["variables"]

        result = col.find_one({"protocol": self.protocol})
        to_return = {}

        if result is not None:
            if moveName in result["variables"]:

                for name, var in result["variables"][moveName].items():
                    #var = result["variables"][moveName]
                    #name = var["name"]
                    value = var["value"]

                    append = False

                    if "append" in var and type(var["append"]) == bool:
                        append = var["append"]

                    if value[0] == "$":
                        if value[1:] in reply:
                            value = reply[value[1:]]

                            #check if the value needs extracted
                            matches = re.findall(self.value_regex, value)

                            if matches:
                                value = matches[0]
                        else:
                            value = ""

                    to_return[name] = {"append": append, "value": value}

        return to_return

    def select_move_content(self, moves):

        possible_content = {}

        for participant, moves in moves.items():
            if participant == "dialogueID":
                continue

            participant_content = {}

            for move in moves:
                moveID = move["moveID"]
                target = move["target"]

                # determine whether or not we need to find content
                variables = False
                for key,value in move["reply"].items():
                    if value[0] == "$":
                        variables = True
                        break

                if not variables:
                    ''' we don't need to find new content, but we might need to
                        find statements for existing content'''
                    reply = move["reply"]

                    if reply != {}:
                        ''' use an ArgumentDescriptor instance to interface with
                            the dictionary'''
                        a = ArgumentDescriptor(self.protocol, self.dialogueID)
                        for key,value in reply.items():
                            content = a.query_dictionary(value, moveID)
                            if content != {}:
                                participant_content[moveID] = [{"reply": move["reply"], "target":target, "openers":content}]
                            else:
                                participant_content[moveID] = [{"reply": move["reply"], "target":target, "openers":{"*":move["opener"]}}] # no content = use whatever "opener" was sent by DGEP
                    else:
                        participant_content[moveID] = [{"reply": move["reply"], "target":target, "openers":{"*":move["opener"]}}] #n o reply object = use whatever "opener" was sent by DGEP

                else:
                    descriptor = self.descriptors_new[moveID]
                    type = descriptor["type"]

                    if type in self.descriptor_handlers:
                        handler = self.descriptor_handlers[type](self.protocol, self.dialogueID)
                        handler.load(descriptor["expression"])
                        content = handler.find_content(move["reply"], moveID)

                        for i in range(len(content)):
                            content[i]["target"] = target

                        if moveID in participant_content:
                            participant_content[moveID].extend(content)
                        else:
                            participant_content[moveID] = content

            possible_content[participant] = participant_content

        return possible_content

    def filter_content(self, participant, moveName, content):
        styles = self.get_move_styles() #{"Francois": "socratic"}

        to_return = []

        if participant in styles:
            style = styles[participant]
        else:
            style = "*";

        for c in content:
            if style in c["openers"]:
                opener = c["openers"][style]
            elif "*" in c["openers"]:
                opener = c["openers"]["*"]
            else:
                opener = c["openers"][list(c["openers"].keys())[0]]

            to_return.append({"reply": c["reply"], "opener": opener, "target":c["target"]})

        return to_return

    def get_dialogue_tags(self):
        return []
