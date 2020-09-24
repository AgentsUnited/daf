import re
import pyaspic
from daf import mongo
from content import *
import dialogue

@content_descriptor
class Argument(ContentDescriptor):

    def __init__(self, *args, **kwargs):
        self.dialogue_id = kwargs["dialogue_id"]
        self.speaker = kwargs["speaker"]

        self.argument_model = {}

        self.history = kwargs["history"]

        # if self.speaker is not None:
        #     col = mongo.get_column("dialogues")
        #     result = col.find_one({"dialogueID": self.dialogue_id})
        #
        #     if result is not None and self.speaker in result["agents"]:
        #         self.argument_model = result["agents"][self.speaker]["knowledge"]

        col = mongo.get_column("argument_models")
        result = col.find_one({"contentID":"abc"})

        self.argument_model = result["model"]
        self.rule_regex = re.compile(r"(\[(?:[^\[\]]+)\])[ ]*(.*)")
        self.theory = self.build_theory()



    def build_theory(self):
        system = pyaspic.ArgumentationSystem()

        all_antecedents = []

        auth_token = dialogue.get_auth_token(self.dialogue_id)

        for rule in self.argument_model.get("rules",[]):
            rule = self.create_aspic_rule(variable_manager.insert_values(auth_token, rule))
            system.add_rule(rule)
            all_antecedents.extend([a[0] for a in term.get_term_specifications(rule.antecedents) if "<" not in a[0]])

        all_antecedents = list(set(all_antecedents))

        for contrary in self.argument_model.get("contrariness", []):
            contradiction = False
            if "-" in contrary:
                symbol = "-"
                contradiction = True
            elif "^" in contrary:
                symbol = "^"
            else:
                continue

            c = contrary.split(symbol)
            for i in range(2):
                c[i] = variable_manager.insert_values(auth_token,c[i])

            system.add_contrary((c[0],c[1]),contradiction)

        for pref in self.argument_model.get("rulePreferences", []):
            p = pref.split("<")
            system.add_rule_preference((p[0].strip(), p[1].strip()))

        kb = pyaspic.KnowledgeBase()

        for t in variable_manager.get_terms(auth_token, all_antecedents):
            kb.add_premise(pyaspic.Formula(t))

        theory = pyaspic.ArgumentationTheory(system, kb)

        return theory.evaluate()


    def find_content(self, query, existing_content=None):
        """
        Use the argumentation theory to find content that matches the given query
        """
        to_return = []
        auth_token = dialogue.get_auth_token(self.dialogue_id)

        if existing_content is None:
            existing_content = {}

        vars_to_fill = []

        if query is not None:
            for key,value in existing_content.items():
                if value[0] != "$":
                    query = query.replace("${}".format(key), value)
                else:
                    vars_to_fill.append(key)

        query = variable_manager.insert_values(auth_token, query)

        if "=>" in query:
            content = []
            elements = query.split("=>")
            conclusion = elements[1].strip()
            premises = elements[0].strip().split(",")

            if conclusion == "[?]":
                pass
            else:
                content = []
                arguments = self.get_arguments_matching_conclusion(conclusion)

                arguments2 = self.get_arguments_with_conclusion(conclusion, True)


                arguments = self.get_arguments_with_conclusion(conclusion, True)
                support = []

                for label,arg in arguments.items():
                    for sub_arg in arg["last_sub_arguments"]:
                        support.append(self.theory["arguments"][sub_arg]["conclusion"])

                if len(support) == len(vars_to_fill):
                    var_map = dict(zip(vars_to_fill, support))
                    statements = []
                    for s in support:
                        spec = term.get_term_specification(s)
                        entry = dictionary.get_entry(self.dialogue_id, spec[0], spec[2])
                        statements.extend(entry)


                    if statements:
                        however = []
                        similar = self.get_similar_arguments(conclusion)

                        for label, arg in similar.items():
                            for sub_arg in arg["last_sub_arguments"]:
                                conclusion = self.theory["arguments"][sub_arg]["conclusion"]
                                spec = term.get_term_specification(conclusion)
                                entry = dictionary.get_entry(self.dialogue_id, spec[0], spec[2])

                                for e in entry:
                                    however.append(e["text"])

                        if however:
                            new_statements = []

                            for s in statements:
                                text = s["text"]
                                properties = s["properties"]
                                for h in however:
                                    new_statement = {"text": "{}. However, {}".format(h, text), "properties": properties}
                                    new_statements.append(new_statement)

                            statements = new_statements

                        to_return.append({"content": {vars_to_fill[0]: support[0]}, "statements": statements})





                        # now look for "however" components

                # arguments = self.get_arguments_matching_conclusion(conclusion)
                #
                # acceptable = [a for a in arguments if a in self.theory["extensions"][0]]
                # unacceptable = [a for a in arguments if a not in acceptable]
                #
                # however = []
                # support = []
                #
                #
                #
                # for a in unacceptable:
                #     s = [self.theory["arguments"][b]["conclusion"] for b in self.theory["arguments"][a]["last_sub_arguments"]]
                #
                #     if len(s) == len(premises):
                #         support.append(s)
                #
                #
                # for i in range(len(support)):
                #     if len(support[i]) == len(vars_to_fill):
                #         for c in support[i]:
                #             content_spec = term.get_term_specification(c)
                #             entry = dictionary.get_entry(self.dialogue_id, content_spec[0],content_spec[2])
                #             however.extend(entry)
                #
                # # need to find non-atomic args that conclude this
                # for a in acceptable:
                #     acceptable_check = [b for b in self.theory["arguments"][a]["last_sub_arguments"] if b in self.theory["extensions"][0]]
                #     if len(acceptable_check) == len(premises):
                #         content.append([self.theory["arguments"][a]["conclusion"] for a in acceptable_check])
                #
                # for i in range(len(content)):
                #     if len(content[i]) == len(vars_to_fill):
                #         var_map = dict(zip(vars_to_fill, content[i]))
                #         s = []
                #
                #         for c in content[i]:
                #             content_spec = term.get_term_specification(c)
                #             entry = dictionary.get_entry(self.dialogue_id, content_spec[0],content_spec[2])
                #             s.extend(entry)
                #
                #         statements = []
                #
                #         if however:
                #             for statement in s:
                #                 statement["text"] = however[0]["text"] + " however " + statement["text"]
                #                 statements.append(statement)
                #         else:
                #             statements = s
                #
                #         to_return.append({
                #             "content": var_map,
                #             "statements": statements
                #         })
        elif query[0] == "[" and query[-1] == "]" and len(vars_to_fill) == 1:
            query = query[1:-1]
            query_spec = term.get_term_specification(query)

            for conclusion in self.theory["acceptableConclusions"][0]:
                conclusion_spec = term.get_term_specification(conclusion)

                if conclusion_spec[0] == query_spec[0] and conclusion_spec[1] == query_spec[1]:
                    entry = dictionary.get_entry(self.dialogue_id, conclusion_spec[0],conclusion_spec[2])

                    to_return.append({"content": {vars_to_fill[0]: conclusion},
                                      "statements": entry
                                    })

        return to_return


    def create_aspic_rule(self, rule):
        '''
        Create a pyaspic rule from the given "[label] rule" string
        '''
        print("Trying to create aspic rule: " + str(rule))
        matches = re.findall(self.rule_regex, rule.strip())

        if matches:
            return pyaspic.Rule.from_string(matches[0][0],matches[0][1])
        else:
            return None

    def get_arguments_with_conclusion(self, conclusion, acceptable=False):
        if acceptable:
            return {label:argument for label, argument in self.theory["arguments"].items() if argument["conclusion"]==conclusion and label in self.theory["extensions"][0]}
        else:
            return {label:argument for label, argument in self.theory["arguments"].items() if argument["conclusion"]==conclusion}

    def get_similar_arguments(self, input, acceptable=False):
        similar = {}

        input_spec = term.get_term_specification(input)

        print("Input spec: " + str(input_spec))

        for label, arg in self.theory["arguments"].items():
            conclusion = arg["conclusion"]

            if input == conclusion:
                continue

            conclusion_spec = term.get_term_specification(conclusion)
            print("Conclusion spec: " + str(conclusion_spec))

            if input_spec[0] == conclusion_spec[0] and input_spec[1] == conclusion_spec[1]:
                similar[label] = arg

        return similar

    def get_arguments_matching_conclusion(self, input):
        to_return = []
        input_spec = term.get_term_specification(input)

        for label, arg in self.theory["arguments"].items():
            conclusion = arg["conclusion"]

            if conclusion == input:
                continue

            arg_conclusion_spec = term.get_term_specification(conclusion)

            if input_spec[0] == arg_conclusion_spec[0] and input_spec[1] == arg_conclusion_spec[1]:
                to_return.append(label)

        return to_return
