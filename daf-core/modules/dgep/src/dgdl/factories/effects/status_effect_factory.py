from .effect_factory import EffectFactory
from ....defcon.effects.status_effect import Status_Effect

class StatusEffectFactory(EffectFactory):

    def __init__(self, tree):

        #print("STATUS EFFECT")
        effect_type = tree.getChildren()[0].getText()

        self.effect = Status_Effect(effect_type)
