
class Participant:

    def __init__(self, participantID, player_template, player_name=None):

        self.participantID = participantID
        self.playerID = player_template.playerID
        self.roles = player_template.roles

        if self.playerID not in self.roles:
            self.roles.append(self.playerID)
        self.name = player_name

        return

    def in_role(self, role_name):
        return role_name in self.roles

    def add_role(self, role_name):
        if role_name not in self.roles:
            self.roles.append(role_name)

    def del_role(self, role_name):
        if role_name != self.playerID and role_name in self.roles:
            self.roles.remove(role_name)

    def __str__(self):
        return str({"participantID": self.participantID,
                "name": self.name,
                "roles": self.roles})
        #return str(self.participantID) + ") (" + str(self.name) + ") Roles: " + str(self.roles)
