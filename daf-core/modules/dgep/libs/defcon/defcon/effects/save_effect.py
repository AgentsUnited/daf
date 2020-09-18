from .effect import Effect
import copy

class Save_Effect(Effect):

    def __init__(self, content, var_name):
        self.type = "save"
        self.content = content
        self.name = var_name

    def perform(self, system, interaction_data=None):

        if not interaction_data:
            system.runtime_vars[self.name] = self.content
        else:
            content = interaction_data["content"]
            if content:
                if self.content == '...':
                    system.runtime_vars[self.name] = []
                    for k in list(content.keys()):
                        index = int(k[3:])
                        system.runtime_vars[self.name].insert(index,content[k])
                else:
                    if "reply" in content:
                        content = content["reply"]
                        for k in list(content.keys()):
                            if len(k) > 3 and k[:3] == '...':
                                    s = copy.deepcopy(self)

                            elif k == self.content:
                                self.content = content[k]
                                break

                        system.runtime_vars[self.name] = self.content
