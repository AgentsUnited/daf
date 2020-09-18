from ....defcon.effects.effect import Effect

class EffectFactory:

    def __init__(self, tree):
        self.effect = Effect()

    def get_effect(self):
        return self.effect
