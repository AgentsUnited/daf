from .effect import Effect
from ..external.external import ExternalURI

class Receive_Effect(Effect):

    def __init__(self, identifier, var_name=None):
        self.type = "receive"

        self.identifier = identifier
        self.var_name = var_name

    def perform(self, system, interaction_data=None):
        if self.identifier in system.ext_uri_map:
            value = ExternalURI().get(system.ext_uri_map[self.identifier])
            if self.var_name:
                system.runtime_vars[self.var_name] = value
