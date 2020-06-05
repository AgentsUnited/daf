import re
import pymongo
import os

class ContentDescriptorLoader:

    def __init__(self, protocol):
        self.descriptor_regex = re.compile(r"(([A-Za-z]+){[\n\r\t ]*([a-z]+){([^{}]+)}[;]?[\n\r\t ]*})+", flags=re.MULTILINE)
        self.descriptors = {}

        database = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        db = mongo[database]
        col = db["content_descriptors"]

        result = col.find_one({"protocol": protocol.lower()})

        if "descriptors" in result.keys():
            for name, description in result["descriptors"].items():
                self.descriptors[name] = description

        '''with open(src) as file:
            matches = re.findall(self.descriptor_regex, file.read())

            for match in matches:
                self.descriptors[match[1]] = {"type": match[2], "expression": match[3]}'''

    def get_descriptors(self):
        return self.descriptors
