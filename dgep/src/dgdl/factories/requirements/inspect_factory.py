from .requirement_factory import RequirementFactory
from ....defcon.requirements.inspect import InspectRequirement

class InspectRequirementFactory(RequirementFactory):

    def __init__(self, tree):

        children = tree.getChildren()

        self.commitments = []

        position = children[0].text
        self.process_commitments(children[1])
        store_name = children[2].text
        user = None
        time = None

        for i in range(3, len(children)):
            child = children[i]
            label = child.text

            if label == "USER":
                user = child.getChildren()[0].text
            elif label == "TIME":
                time = child.getChildren()[0].text

        self.requirement = InspectRequirement(position, store_name, self.commitments, user, time)

    def process_commitments(self, tree):
        for c in tree.getChildren():
            self.commitments.append(c.text)
