from .requirements import get_requirement_handler
from .effects import get_effect_handler
from ...defcon.conditional import Conditional

class ConditionalFactory:

    def __init__(self, tree):

        self.conditional = Conditional()

        #print("Conditional tree: " + tree.toStringTree())

        in_else = False

        for child in tree.getChildren():
            label = child.text

            if label == "REQUIREMENTS":
                self.add_requirements(child)
            elif label == "EFFECTS" and not in_else:
                self.add_effects(child)
            elif label == "CONDITIONAL":
                self.conditional.elseif_ = ConditionalFactory(child).get_conditional()
            elif label == "else":
                in_else = True
            elif label == "EFFECTS" and in_else:
                self.add_else_effects(child)

    def add_requirements(self, tree):
        '''Adds the requirements described by the given tree'''

        for r in tree.getChildren():
            if r.text == "&":
                continue
            req = get_requirement_handler(r)
            if req:
                self.conditional.requirements.append(req)

    def add_effects(self, tree):
        '''Adds the 'if' effects described by the given tree'''

        for e in tree.getChildren():
            effect = get_effect_handler(e)
            if effect:
                self.conditional.effects.append(effect)

    def add_else_effects(self, tree):
        '''Adds the 'else' effects described by the given tree'''

        for e in tree.getChildren():
            # Use an effects factory to get build the effect
            #effect = Effect_factory(e).get_effect()
            effect = get_effect_handler(e)
            if effect:
                self.conditional.else_effects.append(effect)

    def get_conditional(self):
        return self.conditional
