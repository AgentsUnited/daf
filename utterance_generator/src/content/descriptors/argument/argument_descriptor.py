from .. import ContentDescriptor
from .argumentation_theory import ArgumentationTheory
from .argument_dictionary import ArgumentDictionary
from ...skb import SKB
import re

class ArgumentDescriptor(ContentDescriptor):

    def __init__(self, protocol, dialogueID):
        self.query = None

        self.arg_regex = re.compile(r"(A[0-9]+):[ ]*([^-=>\n\r]+)(?:(?:=>|->)([^\n\r]+))?")
        self.term_regex = re.compile(r"(.*)\(([a-zA-z,_0-9? ]+)\)")

        self.skb_regex = re.compile(r"{([^{}]+)}")

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

        however = []

        #TODO: fix bug that stops existing content being passed through

        existing_content = {}

        if self.query is not None:
            for key,value in vars.items():
                if value[0] != '$':
                    self.query = self.query.replace('$' + key, value)
                    existing_content[key] = value
                else:
                    vars_to_fill.append(key)

        # replace any skb variables used in the query
        matches = re.findall(self.skb_regex, self.query)

        if matches:
            skb = SKB(dialogueID=self.dialogueID)
            for m in matches:
                value = skb.get_variable_value(m)
                if m in value:
                    self.query = self.query.replace("{" + m + "}", value[m])

        if "=>" in self.query:
            elements = self.query.split("=>")

            conclusion = elements[1].strip()
            premises = elements[0].strip().split(",")

            if conclusion == "[?]":
                pass
            else:
                arguments = self.get_arguments_with_conclusion(conclusion)
                similar = self.get_similar_arguments(conclusion)

                for arg in arguments:
                    defeated = []
                    args = {s: self.at["arguments"][s] for s in arg["last_sub_arguments"] if self.is_statement(self.at["arguments"][s]["conclusion"]) and s in self.at["extensions"][0]}
                    conclusions = [c["conclusion"] for c in args.values()]

                    if len(conclusions) == len(premises):
                        content.append(list(set(conclusions)-set([a for a in conclusions for b in premises if a==b or self.compare(a,b)])))

                        for s in similar:
                            defeated.extend([self.at["arguments"][x]["conclusion"] for x in s["sub_arguments"] if self.defeats(arg["label"], s["label"])])
                        however.append(defeated)

        elif self.query == "[?]":
            # this is just any acceptable conclusion but we need to transform into a list of lists
            content = [[a] for a in self.at["acceptableConclusions"][0]]
            however.append([])
        elif self.query[0] == "[" and self.query[-1] == "]":
            query = self.query[1:-1]
            for conclusion in self.at["acceptableConclusions"][0]:
                if conclusion == query or self.compare(conclusion, query):
                    content.append([conclusion])
                    however.append([])

        to_return = []

        for i in range(len(content)):
            c = content[i]
            h = however[i]
            if len(c) == len(vars_to_fill):
                for j in range(len(c)):
                    # get the text from the dictionary
                    openers = self.query_dictionary(c[j], move_name)

                    # also get text for the "howevers"
                    h2 = [self.query_dictionary(s, move_name) for s in h]

                    if h:
                        for key, value in openers.items():
                            however_clause = " and ".join([h[key] for h in h2 if key in h])

                            if however_clause[0].islower():
                                however_clause = however_clause.capitalize()

                            value = value.lower()

                            openers[key] = however_clause + ", however " + value

                    if openers != {}:
                        reply = {vars_to_fill[j]: c[j]}

                        for k,v in existing_content.items():
                            reply[k] = v
                        to_return.append({"reply": reply, "openers": openers})

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
            if arg["sub_arguments"]:
                if conclusion == arg["conclusion"]:
                    if acceptable and arg["conclusion"] not in self.at["acceptableConclusions"][0]:
                        continue

                    arg["label"] = label
                    arguments.append(arg)

        return arguments

    def get_statement(self, input):
        matches = re.findall(self.term_regex, input)

        if matches:
            return matches[0][0]
        else:
            return None

    def get_similar_arguments(self, conclusion):
        """
        Get arguments with a similar conclusion
        """
        arguments = []

        s = self.get_statement(conclusion)

        if s is None:
            return arguments

        for label, arg in self.at["arguments"].items():
            conclusion = arg["conclusion"]
            if conclusion[:len(s)] == s:
                arg["label"] = label
                arguments.append(arg)

        return arguments


    def defeats(self, arg1, arg2):
        arg1 = arg1.strip()
        arg2 = arg2.strip()

        d1 = "({arg1},{arg2})".format(arg1=arg1,arg2=arg2)
        d2 = "({arg2},{arg1})".format(arg1=arg1,arg2=arg2)

        return d1 in self.at["defeat"] and d2 not in self.at["defeat"]

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
