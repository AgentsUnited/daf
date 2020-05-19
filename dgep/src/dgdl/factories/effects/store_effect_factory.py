from .effect_factory import EffectFactory
from ....defcon.effects.store_effect import Store_Effect

class StoreEffectFactory(EffectFactory):

    def __init__(self, tree):

        children = tree.getChildren()

        action = children[0].text
        content = {}

        for c in children[1].getChildren():
            content[c.text] = c.text

        name = children[2].text
        user = children[3].text
        
        self.effect = Store_Effect(action, content, name, user)
