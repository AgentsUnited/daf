from .requirement_factory import RequirementFactory
from ....defcon.requirements.extCondition import External_Condition

def ExternalConditionFactory(RequirementFactory):

    def __init__(self, tree):
        children = tree.getChildren()

        identifier = children[0].text

        self.requirement = External_Condition(identifier)

        if len(children) > 1:
            for c in children[1].getChildren():
                self.requirement.content[c.text] = c.text
