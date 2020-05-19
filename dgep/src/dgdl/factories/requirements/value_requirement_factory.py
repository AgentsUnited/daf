from .requirement_factory import RequirementFactory
from ....defcon.requirements.value import ValueRequirement

class ValueFactory(RequirementFactory):

    def __init__(self, tree):

        self.requirement = ValueRequirement()
        children = tree.getChildren()

        if children[0].text == "CONTENT":
            self.requirement.value = children[0].getChildren()[0].text
            self.requirement.string_literal = False
        else:
            self.requirement.value = children[0].text
            self.requirement.string_literal = True

        if len(children) > 1:

            if children[1].text == "VAR":
                runtime_var_tree = children[1].getChildren()
                if runtime_var_tree[0].text == "!":
                    self.requirement.negate = True
                    self.requirement.runtime_var = runtime_var_tree[2].text
                elif runtime_var_tree[0].text == "$":
                    self.requirement.negate = False
                    self.requirement.runtime_var = runtime_var_tree[1].text
            elif children[1].text == "!":
                self.requirement.negate = True
                self.requirement.compare_value = children[2].text
            else:
                self.requirement.compare_value = children[1].text
