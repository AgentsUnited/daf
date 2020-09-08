import mongo
import re
import dialogue
from content import variable_manager, term, dictionary

_condition_handlers = {}

def condition_handler(condition):
    def wrapper(fn):
        _condition_handlers[condition] = fn
        return fn
    return wrapper

class Statement:

    def __init__(self, dialogue_id, move, descriptors, history):
        self.condition_handlers = {
            "lastmove": self.check_last_move,
            "previousmove": self.check_previous_move
        }

        self.dialogue_id = dialogue_id
        self.move = move
        self.descriptors = descriptors
        self.history = history

        # regexes

        # checks for statements of the form foo(bar,...)
        self.statement_regex = re.compile(r"([^\(\) ]+)(?:\(([^\()]+)\))?")

    def find_statements(self):
        statement = None
        statements = []

        print(self.descriptors)

        for key, value in self.descriptors.items():
            if key == "default" and statement is None:
                statement = value
            else:
                if ":" in key:
                    condition = key.split(":")
                    if condition[0] in self.condition_handlers:
                        if self.condition_handlers[condition[0]](condition[1]):
                            statement = value
                            break

        if statement is None:
            return []

        print("Found statement: " + statement)

        # check for statement structure
        matches = re.findall(self.statement_regex, statement)

        if matches:
            match = matches[0]
            statement = match[0]

            statement = variable_manager.insert_values(dialogue.get_auth_token(self.dialogue_id), statement)

            if len(match) == 2 and match[1] != "":
                parameters = self.populate_parameters(dict(x.split(":") for x in match[1].split(",")))
            else:
                parameters = []

            statements = dictionary.get_entry(self.dialogue_id, statement, parameters)
        return statements

    def populate_parameters(self, parameters):
        '''
        Gets values for parameters based on the existing content
        '''
        to_return = []

        for parameter, value in parameters.items():
            value = int(value)
            if parameter in self.move.get("reply",{}):
                tmp = self.move["reply"][parameter]

                spec = term.get_term_specification(tmp)
                if spec[1] >= value:
                    to_return.append(spec[2][value-1])

        return to_return

    def check_last_move(self, moveID):
        """
        Checks if the last move in the dialogue corresponds to moveID
        Is simple a wrapper for check_previous_move with {1} as a parameter
        """
        return self.check_previous_move(moveID + "{1}")

    def check_previous_move(self, moveID):
        """
        Checks if the given moveID is a previous move in the dialogue
        If {n} is appended to the end of the move, the check determines
        if the move is n moves previous (e.g. {1} = the last move; {2} = second last move etc.)
        """
        history_size = len(self.history)

        if moveID[0] == "!":
            moveID = moveID[1:]
            negate = True
        else:
            negate = False

        result = False

        if history_size > 0:
            moveID = moveID.lower()

            regex = re.compile(r"([^{}]+){(\d+)}")
            matches = re.findall(regex, moveID)

            if matches:
                moveID = matches[0][0]
                lookback = int(matches[0][1])

                if history_size >= lookback:
                    move = self.history[lookback * -1]
                    if "moveID" in move:
                        if move["moveID"].lower() == moveID:
                            result = True
            else:
                for move in self.history:
                    if "moveID" in move:
                        if move["moveID"].lower() == moveID:
                            result = True
                            break

        if negate:
            return not result
        else:
            return result
