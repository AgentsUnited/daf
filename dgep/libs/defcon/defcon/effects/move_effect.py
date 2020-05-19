from .effect import Effect
#from ..requirements import get_requirement_handler
from ..move import Move
import copy

class Move_Effect(Effect):

    def __init__(self, action, time, id, content=None, user=None, addressee=None, requirements=None, opener=None):

        self.type = "move"

        self.action = action
        self.time = time
        self.id = id

        if content is None:
            self.content = []
        else:
            self.content = content

        self.user = user
        self.addressee = addressee

        if requirements is None:
            self.requirements = []
        else:
            self.requirements = requirements

        self.opener = opener

    def perform(self, system, interaction_data=None):

        perform = True
        new_content = None

        print("CONTENT: " + self.id + " " + str(self.content))

        # if this move does not exist an interaction, do nothing
        if self.id not in list(system.interactions.keys()):
            print("Warning: move " + self.id + " does not exist as an interaction; skipping")
            return

        print("XXXXX")
        print(interaction_data);

        if interaction_data:
            if self.user == "Target":
                self.user = interaction_data["target"]

            content = interaction_data["content"]["reply"]

            print("Content in move effect interaction data: " + str(content))
            print("Content in move effect itself: " + str(self.content))

            if content:
                for i in range(0,len(self.content)):
                    key = list(self.content[i].keys())[0]
                    if key == "VAR":
                        continue;

                    for k in list(content.keys()):
                        print("Content key: " + k)
                        if len(k) > 3 and k[:3] == '...':
                            if self.content[i][key] == "$...":
                                if new_content is None:
                                    new_content = ""
                                new_content = new_content + ", " + content[k]
                            else:
                                m = copy.deepcopy(self)
                                m.perform(system, {'content':{'...': content[k]}})
                                perform = False
                        elif k == key and content[key][:1] != "$":
                            if self.content[i][key][:1] == "!":
                                self.content[i][key] = "!" + content[k]
                            else:
                                self.content[i][key] = content[k]

        print(self.content)

        if not perform:
            return

        if new_content is not None:
            self.content[i][key] = new_content

        # Check that the requirements are fulfilled
        fulfilled = True
        for r in self.requirements:
            if not r.test(system, interaction_data):
                fulfilled = False
                break

        if fulfilled:
            if self.action == "add":
                system.add_move(self.user, self)
            elif self.action == "delete":
                #self.delete_move(role, move)
                return
