from .. import ContentDescriptor
from .argumentation_theory import ArgumentationTheory
from .argument_dictionary import ArgumentDictionary
import re

class ArgumentDescriptor(ContentDescriptor):

    def __init__(self, protocol, dialogueID):
        self.query = None

        self.arg_regex = re.compile(r"(A[0-9]+):[ ]*([^-=>\n\r]+)(?:(?:=>|->)([^\n\r]+))?")
        self.term_regex = re.compile(r"(.*)\(([a-zA-z,_0-9? ]+)\)")

        self.dictionary = ArgumentDictionary(dialogueID, protocol, "EN")

        self.protocol = protocol

        self.dialogueID = dialogueID

    def load(self, term):
        self.query = term

        a = ArgumentationTheory(self.dialogueID)
        a.load_argument_model(self.protocol)

        self.at = a.evaluate()

    def find_content(self, vars, move_name):

        content = []
        vars_to_fill = []

        if self.query is not None:
            for key,value in vars.items():
                if value[0] != '$':
                    self.query = self.query.replace('$' + key, value)
                else:
                    vars_to_fill.append(key)

        if "=>" in self.query:
            elements = self.query.split("=>")

            conclusion = elements[1].strip()
            premises = elements[0].strip().split(",")

            if conclusion == "[?]":
                pass
            else:
                arguments = self.get_arguments_with_conclusion(conclusion)

                for arg in arguments:
                    conclusions = [self.at["arguments"][s]["conclusion"] for s in arg["subargs"] if self.is_statement(self.at["arguments"][s]["conclusion"]) and self.at["arguments"][s]["conclusion"] in self.at["acceptableConclusions"]["0"]]

                    if len(conclusions) == len(premises):
                        content.append(list(set(conclusions)-set([a for a in conclusions for b in premises if a==b or self.compare(a,b)])))
        elif self.query == "[?]":
            # this is just any acceptable conclusion but we need to transform into a list of lists
            content = [[a] for a in self.at["acceptableConclusions"]["0"]]
        elif self.query[0] == "[" and self.query[-1] == "]":
            query = self.query[1:-1]
            for conclusion in self.at["acceptableConclusions"]["0"]:
                if conclusion == query or self.compare(conclusion, query):
                    content.append([conclusion])

        to_return = []

        for c in content:
            if len(c) == len(vars_to_fill):
                for i in range(len(c)):
                    # get the text from the dictionary
                    openers = self.query_dictionary(c[i], move_name)
                    print("Openers: " + str(openers))
                    if openers != {}:
                        to_return.append({"reply": {vars_to_fill[i]: c[i]}, "openers": openers})

        # [{"reply":{"p":"<content>"}, "opener":{styleName: str}}]
        return to_return

    def is_statement(self, term):
        if re.findall(self.term_regex, term):
            return True
        else:
            return False

    def query_dictionary(self, content, move_name):

        move_name = move_name.lower()

        var_value = None

        if self.is_statement(content):
            match = re.findall(self.term_regex, content)[0]

            content = match[0] + "(X)"
            var_value = match[1]

        result = self.dictionary.query(content)

        if result != {}:
            if move_name in result:
                if var_value is not None:
                    for k in result[move_name]:
                        result[move_name][k] = result[move_name][k].replace("$X", var_value)

                return result[move_name]

        return {}

    def get_arguments_with_conclusion(self, conclusion, acceptable=True):

        arguments = []

        for label,arg in self.at["arguments"].items():
            if arg["subargs"]:
                #if self.compare(conclusion, arg["conclusion"]):
                if conclusion == arg["conclusion"]:
                    if acceptable and arg["conclusion"] not in self.at["acceptableConclusions"]["0"]:
                        continue

                    arguments.append(arg)

        return arguments

    def compare(self, value1, value2):
        matches = re.findall(self.term_regex, value1)

        if matches:
            value1_match = list(matches[0])

            matches = re.findall(self.term_regex, value2)

            if matches:
                value2_match = list(matches[0])

                value1_vars = value1_match[1].split(",")
                value2_vars = value2_match[1].split(",")

                if value1_match[0] == value2_match[0] and len(value1_vars) == len(value2_vars):
                    return True

        # if we get this far we can only return false
        return False
