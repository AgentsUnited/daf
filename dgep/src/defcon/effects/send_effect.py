from .effect import Effect
from ..external.external import ExternalURI

class Send_Effect(Effect):

    def __init__(self, identifier):
        self.type = "send"

        self.identifier = identifier
        self.vars = {}
        self.content_sets = []

    def update(self, system=None, update_data=None):

        if update_data:
            content = update_data["content"]

            for variable,val in self.vars.items():
                if variable in self.content_sets:
                    for i in range(0,len(val)):
                        for key,value in content.items():
                            if val[i] == key:
                                val[i] = content[key]
                                continue
                    self.vars[variable] = ",".join(val)

                else:
                    if val[0] == "$":
                        self.vars[variable] = system.get_runtime_var(val[1:])

                    for key,value in content.items():
                        if val == key:
                            self.vars[variable] = content[key]

    def perform(self, system, interaction_data=None):
        #print("Performing send effect")
        self.update(system, interaction_data)
        if self.identifier in system.ext_uri_map:
            ExternalURI().call(system.ext_uri_map[self.identifier], self.vars)
