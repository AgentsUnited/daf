from .requirement_factory import RequirementFactory
from ....defcon.requirements.player import Player

class PlayerFactory(RequirementFactory):

    def __init__(self, tree):
        player = tree.getchildren()[0].text

        self.requirement = Player(player)
