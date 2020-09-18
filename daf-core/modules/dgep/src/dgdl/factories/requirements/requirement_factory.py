from ....defcon.requirements.requirement import Requirement

class RequirementFactory:

    def __init__(self, tree):
        self.requirement = Requirement()

    def get_requirement(self):
        return self.requirement
