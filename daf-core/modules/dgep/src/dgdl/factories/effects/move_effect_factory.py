from ....defcon.effects.move_effect import Move_Effect
from .effect_factory import EffectFactory
from ..requirements import get_requirement_handler

class MoveEffectFactory(EffectFactory):

    def __init__(self, tree):

        children = tree.getChildren()

        action = children[0].text
        time = children[1].text
        id = children[2].text

        self.effect = Move_Effect(action, time, id)
        self.content = []
        self.user = None
        self.addressee = None
        self.requirements = []

        for i in range(3, len(children)):
            label = children[i].text

            if label == "$":
                self.effect.addressee = children[i].getChildren()[0].text
            elif label == "CONTENT":
                self.add_content(children[i])
            elif label == "REQUIREMENTS":
                self.add_requirements(children[i])
            elif label == "OPENER":
                self.effect.opener = children[i].getChildren()[0].text
            else:
                self.effect.user = label

    def add_content(self, tree):
        '''Add the specified content to this move
            Because dictionaries don't preserve the order, each content
            is its own dict in a list'''

        negate = False

        for c in tree.getChildren():
            if c.text == "!":
                negate = True
                continue

            if c.text == "VAR":
                value = c.getChildren()[0].text
                if value == "!":
                    negate = True
                    value = c.getChildren()[2].text
                else:
                    value = c.getChildren()[1].text
            else:
                value = c.text

                if value[-3:] != "...":
                    value = "$" + value

            if negate:
                value = "!" + value

            self.effect.content.append({c.text:value})

    def add_requirements(self, tree):
        '''Add the requirement(s) to this move'''
        for r in tree.getChildren():
            if r.text != "&":
                requirement = get_requirement_handler(r)
                self.effect.requirements.append(requirement)
