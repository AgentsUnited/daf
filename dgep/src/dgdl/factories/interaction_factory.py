from ...defcon.interaction import Interaction
from .conditional_factory import ConditionalFactory
from .effects import get_effect_handler

class InteractionFactory:

    def __init__(self, tree):

        self.interaction = Interaction(id=tree.getChildren()[0].text)

        for i in range(1, len(tree.getChildren())):
            child = tree.getChildren()[i]
            label = child.text

            if label == "$":
                self.interaction.addressee = child.getChildren()[0].text
            elif label == "TARGET":
                self.add_target(child)
            elif label == "OPENER":
                self.interaction.opener = child.getChildren()[0].text
            elif label == "CONDITIONAL":
                self.interaction.conditional = ConditionalFactory(child).get_conditional()
            elif label == "EFFECTS":
                self.add_effects(child)

    def add_target(self, tree):
        ''' Method to get the target set from the interaction'''

        content = tree.getChildren()[0]

        for c in content.getChildren():
            print("Adding target: " + c.text + " for interaction " + self.interaction.id)
            self.interaction.target.append(c.text)

    def add_force_target(self, tree):
        '''Method to add force targets from the given tree'''

        self.interaction.force_targets.append(Force_target(tree))
        return

    def add_effects(self, tree):
        '''Method to add effects from the given tree'''

        for e in tree.getChildren():
            #self.effects.append(Effect_factory(e).get_effect())
            self.interaction.effects.append(get_effect_handler(e))


    def get_interaction(self):
        return self.interaction
