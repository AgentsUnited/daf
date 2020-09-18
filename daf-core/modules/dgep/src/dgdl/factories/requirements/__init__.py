from .requirement_factory import RequirementFactory
from .role_inspection_factory import RoleInspectionFactory
from .player_factory import PlayerFactory
from .event_factory import EventFactory
from .inspect_factory import InspectRequirementFactory
from .external_condition_factory import ExternalConditionFactory
from .value_requirement_factory import ValueFactory

requirements = {
    "event": EventFactory,
    "inspect": InspectRequirementFactory,
    "inrole": RoleInspectionFactory,
    #"size": RequirementFactory,
    #"magnitude": RequirementFactory,
    "player": PlayerFactory,
    "extCondition": ExternalConditionFactory,
    "value": ValueFactory
}

def get_requirement_handler(tree):
    requirement = tree.text
    if requirement in list(requirements.keys()):
        requirement = requirements[requirement](tree)
    else:
        requirement = RequirementFactory(tree)

    return requirement.get_requirement()
