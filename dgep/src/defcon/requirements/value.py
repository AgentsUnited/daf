from .requirement import Requirement

class ValueRequirement(Requirement):

    def __init__(self):
        self.type = "value"

        self.runtime_var = None
        self.negate = False

        self.compare_value = None

    def test(self, system, interaction_data = None):

        if self.string_literal:

            if self.runtime_var:
                self.compare_value = system.get_runtime_var(self.runtime_var)

            if self.negate:
                self.compare_value = "not " + self.runtime_var

            print("Comparing " + str(self.compare_value) + " with " + str(self.value))


            if self.compare_value is None:
                return True
            else:
                return self.compare_value.replace('"','') == self.value.replace('"','')
        else:
            content = interaction_data["content"]

            print("TESTING")
            print(self.compare_value)

            if content:
                if self.value in list(content.keys()):
                    self.value = content[self.value]

                    if self.runtime_var:
                        self.compare_value = system.get_runtime_var(self.runtime_var)

                    if self.negate:
                        self.compare_value = "not " + self.runtime_var

                    print(self.compare_value)

                    if self.compare_value is None:
                        print("Returning false because compare value isn't none")
                        return True
                    else:
                        print("Comparing " + str(self.compare_value) + " with " + str(self.value))
                        return self.compare_value.replace('"','') == self.value.replace('"','')
                else:
                    print ("Returning false because self.value isn't there")
                    return False
            else:
                print("Returning false because there's no content")
                return False
