from .requirement_factory import RequirementFactory
from ....defcon.requirements.event import Event

class EventFactory(RequirementFactory):

    def __init__(self, tree):
        children = tree.getChildren()

        position = children[0].text
        moveID = children[1].text

        self.requirement = Event(position, moveID)

        for i in range(2, len(children)):
            child = children[i]
            label = child.text

            if label == "CONTENT":
                self.set_content(child)
            elif label == "REQUIREMENTS":
                self.add_requirements(child)
            else:
                self.requirement.speaker = label

    def set_content(self, tree):
        for c in tree.getChildren():
            self.requirement.content.append(c.text)

    def add_requirements(self, tree):
        from ..requirements import get_requirement_handler
        for r in tree.getChildren():
            requirement = get_requirement_handler(r)
            self.requirement.requirements.append(r)
