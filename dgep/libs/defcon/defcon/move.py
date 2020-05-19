
class Move(object):

    def __init__(self):
        self.action = ""
        self.time = ""
        self.id = ""
        self.requirements = []
        self.addressee = None
        self.user = None

    def __repr__(self):
        string = "\nMoveID: " + self.id
        string += "\nAction: " + self.action
        string += "\nTime: " + self.time
        string += "\nRequirements: " + str(self.requirements)
        string += "\nAddressee: " + str(self.addressee)
        string += "\nUser: " + str(self.user)
        string += "\nContent: " + str(self.content)
        string += "\n"

        return string
