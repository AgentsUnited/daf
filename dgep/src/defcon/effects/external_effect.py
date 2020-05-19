from .effect import Effect
from ..external.external import ExternalURI

class External_Effect(Effect):

    def __init__(self, identifier):
        self.type = "exteffect"
        
        self.identifier = identifier
        self.content = {}


    def update(self, system=None, update_data=None):

        content = update_data["content"]

        if content:
            for k in list(content.keys()):
                if k in list(self.content.keys()) and content[k][:1] != "$":
                        self.content[k] = content[k]

    def perform(self, system, interaction_data=None):
        if self.identifier in system.ext_uri_map:
            ExternalURI().call(system.ext_uri_map[self.identifier], self.content)
