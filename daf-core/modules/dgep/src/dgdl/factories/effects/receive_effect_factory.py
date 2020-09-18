from ....defcon.effects.receive_effect import Receive_Effect
from .effect_factory import EffectFactory

class ReceiveEffectFactory(EffectFactory):

    def __init__(self, tree):

        children = tree.getChildren()

        identifier = children[0].text
        var_name = None

        if len(children) > 1:
            var_name = children[1].getChildren()[1].text

        self.effect = Receive_Effect(identifier, var_name)
