import re

class ContentDescriptorLoader:

    def __init__(self, src):
        self.descriptor_regex = re.compile(r"(([A-Za-z]+){[\n\r\t ]*([a-z]+){([^{}]+)}[;]?[\n\r\t ]*})+", flags=re.MULTILINE)
        self.descriptors = {}

        with open(src) as file:
            matches = re.findall(self.descriptor_regex, file.read())

            for match in matches:
                self.descriptors[match[1]] = {"type": match[2], "expression": match[3]}

    def get_descriptors(self):
        return self.descriptors
