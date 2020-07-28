from ...skb import SKB
import requests
import re
import json
import pymongo
import os

class ArgumentationTheory:

    def __init__(self, dialogueID):
        self.toast_url = "http://toast:1234/evaluate?general=true"

        self.arg_regex = re.compile(r"(A[0-9]+):[ ]*([^-=>\n\r]+)(?:(?:=>|->)([^\n\r]+))?")

        self.skb_regex = re.compile(r"{([^{}]+)}")

        self.rules = []
        self.premises = []
        self.contrariness = []
        self.kbPrefs = []
        self.rulePrefs = []
        self.dialogueID = dialogueID
        self.defeat = []

    def load_argument_model(self, protocol=None):

        #rules = ["dafTestVar(X)=>bar(X)", "bar(X)=>something(X)"]
        db_name = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        col = mongo[db_name]["argument_rules"]

        data = col.find_one({'protocol': protocol})

        if data is not None:
            skb = SKB(dialogueID=self.dialogueID) # efficiency saver
            s = skb.fill_skb_variables
            rules = [s(r) for r in data["rules"]]
            self.contrariness = [s(c) for c in data["contrariness"]]
            self.kbPrefs = [s(p) for p in data["preferences"]]
            rule_preferences = data["rule_preferences"]

        else:
            rules = []
            rule_preferences = []

        print("THE RULES ARE: " + str(rules))

        all_consequents = []
        all_antecedents = []

        current_rule = 0

        for r in rules:
            rule = Rule(r)
            all_consequents.append(rule.consequent)
            all_antecedents.extend(rule.antecedents)
            self.rules.append(rule)

        num_rules = len(self.rules)

        for p in rule_preferences:
            parts = p.split("<")
            lp = int(parts[0].strip())
            mp = int(parts[1].strip())

            if num_rules > lp and num_rules > mp:
                self.rulePrefs.append((lp,mp))

        # get a set of all antecedents that can't be satisfied by rules
        unsatisfiable = list(set([self.get_term(a) for a in all_antecedents if a not in all_consequents]))

        #get premises to satisfy the lhs of contraries
        contraries = list(set([self.get_term(c.split("^")[0].strip()) for c in self.contrariness if "^" in c ]))

        query = list(set(unsatisfiable + contraries))

        print("Query: " + str(query))

        #query the skb for values for those antecedents to use as premises
        skb = SKB(dialogueID=self.dialogueID)
        response = skb.get_variable_values(query)

        print("Response: " + str(response))

        for variable,value in response.items():
            if value is not None:
                if isinstance(value, list):
                    for v in value:
                        self.premises.append("{variable}({value})".format(variable=variable,value=v))
                else:
                    self.premises.append("{variable}({value})".format(variable=variable, value=value))

        print("Premises: " + str(self.premises));

    def evaluate(self):
        theory = {"rules": [], "rulePrefs": []}

        tmp_rules = {}


        print("Rules: " + str(self.rules))

        rule_labels = []

        for i in range(len(self.rules)):
            id = i+1
            label = "[r{id}]".format(id=str(id))
            rule_labels.append(label)
            theory["rules"].append("{label} {rule}".format(label=label, rule=self.rules[i]))
            tmp_rules[id] = self.rules[i]

        for (lp,mp) in self.rulePrefs:
            theory["rulePrefs"].append(rule_labels[lp] + " < " + rule_labels[mp])

        for id1, r1 in tmp_rules.items():
            for id2, r2 in tmp_rules.items():
                if id1==id2:
                    continue

                for k in self.kbPrefs:
                    k = k.split("<")
                    lhs = k[0].strip()
                    rhs = k[1].strip()

                    if self.get_term(r1.antecedents[0]) == self.get_term(lhs) and self.get_term(r2.antecedents[0]) == self.get_term(rhs):
                        theory["rulePrefs"].append("[r{id1}] < [r{id2}]".format(id1=id1,id2=id2))

                #if r1.antecedents[0] + "<" + r2.antecedents[0] in self.kbPrefs:
                    #theory["rulePrefs"].append("[r{id1}] < [r{id2}]".format(id1=id1,id2=id2))

        theory["premises"] = self.premises
        theory["semantics"] = "grounded"
        theory["contrariness"] = self.contrariness
        theory["kbPrefs"] = self.kbPrefs
        theory["link"] = "last"

        print("Theory: " + str(theory))

        result = requests.post(self.toast_url, data=json.dumps(theory))

        result = json.loads(result.text)

        self.defeat = result["defeat"]

        # refactor the set of arguments to make them easier to query
        tmp = {}

        for a in result["arguments"]:
            matches = re.findall(self.arg_regex, a)

            if len(matches) == 1:
                arg = list(matches[0])

                label = arg[0].strip()

                if len(arg) == 2 or arg[2]=='':
                    subargs = []
                    conclusion = arg[1].strip()
                else:
                    subargs = [a.strip() for a in arg[1].split(",")] #use comprehension to trim potential whitespace
                    conclusion = arg[2].strip()

                tmp[label] = {"subargs": subargs, "conclusion": conclusion}

        result["arguments"] = tmp

        print("AT:" + str(result))

        return result


    def defeats(self, arg1, arg2):
        arg1 = arg1.strip()
        arg2 = arg2.strip()

        d1 = "{arg1}>{arg2}".format(arg1=arg1,arg2=arg2)
        d2 = "{arg2}>{arg1}".format(arg1=arg1,arg2=arg2)

        return d1 in self.defeat and d2 not in self.defeat

    def get_term(self, statement):
        matches = re.findall(r"(.*)\(([a-zA-z,_0-9? ]+)\)", statement)

        if matches:
            match = matches[0]
            return match[0]
        else:
            return statement

    def get_premises(self, protocol):
        db_name = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        col = mongo[db_name]["coaching_variables"]

        result = col.find_one()

        premises = []

        for key, value in result.items():
            if key != "_id":
                premises.append("{key}({value})".format(key=key,value=value))

        return premises;



class Rule:

    def __init__(self, str_rule):
        types = {"=>": "defeasible", "->": "strict"}

        self.antecedents = []
        self.type = None
        self.consequent = None
        self.str_rule = ""

        matches = re.findall(r"([^=->]+)(=>|->)([^=->]+)", str_rule)[0]

        if len(matches) == 3:
            self.antecedents = [a.strip() for a in matches[0].split(',')]
            self.type = types[matches[1].strip()]
            self.consequent = matches[2].strip()
            self.str_rule = str_rule

    def __repr__(self):
        return self.str_rule
