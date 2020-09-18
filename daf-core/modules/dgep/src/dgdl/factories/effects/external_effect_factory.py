from .effect_factory import EffectFactory
from ....defcon.effects.external_effect import External_Effect

class ExternalEffectFactory(EffectFactory):

    def __init(self, tree):

        children = tree.getChildren()

        identifier = children[0].text

        self.effect = External_Effect(identifier)

        if len(children) > 1:
            for c in children[1].getChildren():
                self.effect.content[c.text] = c.text
