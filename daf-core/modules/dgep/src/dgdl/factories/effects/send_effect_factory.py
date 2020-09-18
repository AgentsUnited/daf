from ....defcon.effects.send_effect import Send_Effect
from .effect_factory import EffectFactory

class SendEffectFactory(EffectFactory):

    def __init__(self, tree):
        children = tree.getChildren()
        identifier = children[0].text

        self.effect = Send_Effect(identifier)

        if len(children) > 1:

            vars = children[1].getChildren()

            for i in range(0, len(vars)):
                variable = vars[i].getChildren()[0].text
                value = vars[i].getChildren()[1]

                if value.text == "CONTENT":
                    values = []
                    for v in value.getChildren():
                        values.append(v.text)

                    value = values
                    self.effect.content_sets.append(variable)

                elif value.text == "$":
                    value = "$" + vars[i].getChildren()[2].text
                else:
                    value = value.text

                if value[0] == '"':
                    value = value[1:]

                if value[len(value)-1] == '"':
                    value = value[:-1]

                self.effect.vars[variable] = value
