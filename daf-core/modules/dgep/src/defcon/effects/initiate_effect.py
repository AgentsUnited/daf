from .effect import Effect

class Initiate_Effect(Effect):

    def __init__(self, protocol):
        self.type = "initiate"
        self.protocol = protocol

    def perform(self, system, interaction_data=None):
        return system.initiate_new(self.protocol)
