from .requirement_factory import RequirementFactory
from ....defcon.requirements.role_inspection import RoleInspection

class RoleInspectionFactory(RequirementFactory):

    def __init__(self, tree):
        children = tree.getChildren()

        participant = children[0].text
        role = children[1].text

        self.requirement = RoleInspection(participant, role)
