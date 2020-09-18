from .effect import Effect

class Assign(Effect):

    def __init__(self, user, role):
        self.type = "assign"

        self.user = user
        self.role = role

        self.participants = []

    def perform(self, system, interaction_data=None):

        #Determine the participants that are to be assigned to the role
        #If the user is "Target", get them from the update data
        if self.user == "Target" and interaction_data:
            self.participants.append(interaction_data["target"])
        elif self.user == "speaker":
            self.participants.append(system.speaker)
        elif self.user in list(system.players.keys()):

            if self.role == "speaker":
                p = system.players[self.user]

                if p.max == 1:
                    self.participants.append(system.get_participants_in_role(self.user)[0].participantID)
                else:
                    #print("Warning: cannot assign speaker to a Role that can have >1 participant")
            else:
                for p in system.get_participants_in_role(self.user):
                    self.participants.append(p.participantID)

        #If the role is "speaker" don't explictly assign it, just update in the system
        if self.role == "speaker":
            if self.participants and len(self.participants) == 1:
                system.update_speaker(self.participants[0])
        else:
            for u in self.participants:
                system.participants[u].add_role(self.role)

class UnAssign(Effect):

    def __init__(self, user, role):
        self.type = "unassign"

        self.user = user
        self.role = role

    def update(self, update_data=None):
        if self.user == "Target":
            self.user = update_data["target"]

    def perfom(self, system, interaction_data=None):
        if role == "speaker":
            return

        for u in self.participants:
            system.participants[u].del_role(self.role)
