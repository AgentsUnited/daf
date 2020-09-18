from ....defcon.effects.assign import *
from .effect_factory import EffectFactory

class AssignEffectFactory(EffectFactory):

    def __init__(self, tree):

        user = tree.getChildren()[0].text
        role = tree.getChildren()[1].text

        self.effect = Assign(user=user, role=role)

class UnAssignEffectFactory(EffectFactory):

    def __init__(self, tree):

        user = tree.getChildren()[0].text
        role = tree.getChildren()[1].text

        self.effect = UnAssign(user=user,role=role)
