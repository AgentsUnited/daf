from . import ContentDescriptor

class InputDescriptor(ContentDescriptor):

    def __init__(self, protocol=None, dialogueID=None):
        self.var = None


    def load(self, query):
        self.var = query

    def find_content(self, vars, moveID):

        content = []

        for key,value in vars.items():
            if value[0] == "$":
                content.append({"reply": {key: self.var}, "openers":{"*":"{INPUT}"}})

        return content
