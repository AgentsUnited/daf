from .requirement import Requirement
from ..external.external import ExternalURI

class External_Condition(Requirement):

    def __init__(self, identifier):
        children = tree.getChildren()

        self.identifier = identifier
        self.content = {}

    def test(self, system, interaction_data=None):

        if interaction_data:
            content = interaction_data["content"]

            if content:
                for key,value in content.items():
                    if key in list(self.content.keys()):
                        self.content[key] = value

        uri = system.get_uri(self.identifier)

        if uri:
            result = ExternalURI().test(uri, self.content)
        else:
            result = False

        return result
