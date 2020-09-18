from .assign_effect_factory import *
from .effect_factory import EffectFactory
from .move_effect_factory import MoveEffectFactory
from .store_effect_factory import StoreEffectFactory
from .status_effect_factory import StatusEffectFactory
from .external_effect_factory import ExternalEffectFactory
from .send_effect_factory import SendEffectFactory
from .receive_effect_factory import ReceiveEffectFactory
from .invoke_effect_factory import InvokeEffectFactory
#from initiate_effect import Initiate_Effect
from .save_effect_factory import SaveEffectFactory

effects = {
    "assign": AssignEffectFactory,
    "unassign": UnAssignEffectFactory,
    "move": MoveEffectFactory,
    "store": StoreEffectFactory,
    "status": StatusEffectFactory,
    "extEffect": ExternalEffectFactory,
    "send": SendEffectFactory,
    "receive": ReceiveEffectFactory,
    "invoke": InvokeEffectFactory,
#    "initiate": Initiate_Effect,
    "save": SaveEffectFactory
}

def get_effect_handler(tree):
    if tree.text in list(effects.keys()):
        return effects[tree.text](tree).get_effect()
    else:
        return EffectFactory(tree).get_effect()
