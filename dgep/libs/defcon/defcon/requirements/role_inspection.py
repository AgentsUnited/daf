from .requirement import Requirement

class RoleInspection(Requirement):

    def __init__(self, participant, role):
        self.type = "roleinspection"
        self.participant = participant
        self.role = role

    def test(self, system, interaction_data=None):

        #First determine the "participant": is it a player, role or special keyword?
        if self.participant == "Target":
            if interaction_data:
                self.participant = interaction_data["target"]
            else:
                return False #if there's no target, they can't be in the role
        elif self.participant == "speaker":
            self.participant = system.speaker # system tells us the exact participant we need
        elif self.participant in list(system.players.keys()):
                p = system.players[self.participant]
                if p.max == 1:
                    self.participant = system.get_participants_in_role(self.participant)[0].participantID
                else:
                    return False
        else:
            return False #nothing else we can do

        return system.in_role(self.participant, self.role)
