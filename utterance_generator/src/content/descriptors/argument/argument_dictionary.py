import pymongo
import re
import os
from ...skb import SKB

class ArgumentDictionary:

    def __init__(self, dialogueID, protocol, language="EN"):
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")

        database = os.getenv("MONGODB")
        self.dictionary = mongo[database]["dictionary"].find_one({"protocol": protocol.lower()})

        self.var_regex = re.compile(r"(?:[^[]])*{([^{} ]+)}(?:[^[]])*")

        self.dialogueID = dialogueID

    def query(self, query):

        skb = SKB(dialogueID=self.dialogueID)

        if query in self.dictionary["entries"]:
            # check for skb variables

            dict = self.dictionary["entries"][query]

            for moveName, entry in dict.items():
                for style, statement in entry.items():
                    matches = re.findall(self.var_regex, statement)

                    for m in matches:
                        # clean up the statement by making the vars lowercase
                        statement = statement.replace("{{{var}}}".format(var=m), "{{{newvar}}}".format(newvar=m.lower()))

                        m = m.lower()
                        response = skb.get_variable_value(m)
                        if response[m] is None:
                            response[m] = ""

                        statement = statement.replace("{{{var}}}".format(var=m), response[m])

                        dict[moveName][style] = statement

            return dict

        return {}
