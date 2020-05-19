from ...defcon.rule import Rule
from .effects import get_effect_handler
from .conditional_factory import ConditionalFactory


class RuleFactory:

    def __init__(self, tree):

        id = tree.getChildren()[1].text
        self.rule = Rule(id=id)

        #third child is either a conditional or effects
        if tree.getChildren()[2].text == "CONDITIONAL":
            self.rule.conditional = ConditionalFactory(tree.getChildren()[2]).get_conditional()
        elif tree.getChildren()[2].text == "EFFECTS":
            for e in tree.getChildren()[2].getChildren():
                #self.effects.append(Effect_factory(e).get_effect())
                self.rule.effects.append(get_effect_handler(e))

    def get_rule(self):
        return self.rule
