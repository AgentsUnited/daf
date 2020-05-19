from .requirement import Requirement

class Player(Requirement):

    def __init__(self, player):
        self.player = player

    def test(self, system, interaction_data=None):
        return system.is_current_player(self.player)
