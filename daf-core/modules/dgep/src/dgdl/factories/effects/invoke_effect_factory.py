from .effect_factory import EffectFactory
from ....invoke_effect import InvokeEffect

class InvokeEffectFactory(EffectFactory):

    def __init__(self, tree):

        children = tree.getChildren()
        identifier = children[0].text

        self.effect = InvokeEffect(identifier)

        if len(children) > 1:

            vars = children[1].getChildren()

            for i in range(0, len(vars)):
                variable = vars[i].getChildren()[0].text
                value = vars[i].getChildren()[1].text

                if value[0] == '"':
                    self.effect.vars[variable] = value
                else:
                    self.effect.vars[variable] = "$" + value
