import daf
import dialogue
from daf import mongo
import re
from content import Statement, content_locator, variable_manager

@daf.message_handler("DGEP/moves", "UG/response")
class Moves:

    @daf.command_handler("moves")
    @daf.command_handler("interaction")
    def handle_moves(self, command, data):
        print(data)
        dialogue_id = data.get("dialogueID", None)
        session_id = data.get("sessionID", None)

        if dialogue_id is not None:
            moves = data.get("moves", {})
            history = data.get("history", [])

            data["moves"] = self.instantiate_moves(dialogue_id, moves, history)
        return data

    def instantiate_moves(self, dialogue_id, _moves, history):
        """
        Find instantiations of the given moves, whether they require content
        or simply a statement to utter
        """
        instantiated_moves = {}

        for speaker, moves in _moves.items():
            instantiated_moves[speaker] = []
            for move in moves:
                move_id = move["moveID"].lower()

                descriptors = self.get_descriptors(move_id, dialogue_id)

                if descriptors is not None:
                    if self.move_requires_content(move):
                        if "content" in descriptors:
                            content = content_locator.find_content(dialogue_id, speaker, descriptors["content"], move, history)

                            for c in content:
                                new_reply = {}

                                for key, value in move.get("reply",{}).items():
                                    if key not in c["content"]:
                                        new_reply[key] = value

                                new_reply.update(c["content"])

                                variables = variable_manager.get_move_vars(dialogue.get_topic(dialogue_id), move_id, new_reply, dialogue.get_auth_token(dialogue_id))

                                for statement in self.filter_statements(c["statements"], history, dialogue.get_auth_token(dialogue_id)):
                                    new_move = self.build_new_move(move["moveID"],
                                                                   new_reply,
                                                                   statement["text"],
                                                                   move.get("target", ""),
                                                                   variables
                                    )
                                    instantiated_moves[speaker].append(new_move)
                    else:
                        s = Statement(dialogue_id, move, descriptors, history)
                        statements = s.find_statements()
                        variables = variable_manager.get_move_vars(dialogue.get_topic(dialogue_id), move_id, move.get("reply",{}), dialogue.get_auth_token(dialogue_id))
                        for statement in self.filter_statements(statements, history, dialogue.get_auth_token(dialogue_id)):
                            new_move = self.build_new_move(move["moveID"],
                                                           move.get("reply",{}),
                                                           statement["text"],
                                                           move.get("target",""),
                                                           move.get("vars", variables))
                            instantiated_moves[speaker].append(new_move)
        return instantiated_moves


    def move_requires_content(self, move):
        """
        Checks to see if the given move requires content, based on whether or not
        at least one field in the reply has a value starting with '$'
        """
        reply = move.get("reply",{})

        for key,value in reply.items():
            if value[0] == "$":
                return True

        return False

    def get_descriptors(self, move_id, dialogue_id):
        """
        Gets the descriptors for the given move
        """
        topic = dialogue.get_topic(dialogue_id)

        to_return = []

        col = mongo.get_column("content_descriptors")
        result = col.find({"protocol": topic})

        if result is not None:
            for r in result:
                if move_id in r["descriptors"]:
                    return r["descriptors"][move_id]

        return None

    def build_new_move(self, moveID, reply=None, opener="", target="", vars=None):
        """
        Builds a new move based on the given information
        """
        if reply is None:
            reply = {}
        if vars is None:
            vars = {}

        return {
            "moveID": moveID,
            "reply": reply,
            "opener": opener,
            "target": target,
            "vars": vars
        }

    def filter_statements(self, statements, history, auth_token):
        """
        TODO: various filtering methods for statements based on properties
        """

        def fill_statement_variables(statement, history):
            regex = re.compile(r"<<(.*)>>")

            matches = re.findall(regex, statement)

            if matches:
                for m in matches:
                    if m == "lastspeaker":
                        if len(history) > 0:
                            replacement = history[-1]["speaker"]

                            statement = statement.replace("<<{}>>".format(m), replacement)
            return statement

        def check_previous_move(condition, previous_moves):

            negate = False
            result = False

            if condition[0] == "!":
                negate = True
                condition = condition[1:]

            regex = re.compile(r"([^{}]+){(\d+)}")
            matches = re.findall(regex, condition)

            if matches:
                moveID = matches[0][0]
                lookback = int(matches[0][1])

                if len(previous_moves) >= lookback:
                    move = previous_moves[lookback * -1]

                    if move.lower() == moveID.lower():
                        result = True
            else:
                if condition in previous_moves:
                    result = True

            if negate:
                return not result
            else:
                return result

        def check_last_move(condition, previous_moves):
            return check_previous_move(condition + "{1}", previous_moves)

        handlers = {
            "previousmove": check_previous_move,
            "lastmove": check_last_move
        }

        previous_moves = [m["moveID"].lower() for m in history]

        properties_satisfied = [0] * len(statements)

        highest = 0

        i = 0
        for statement in statements:
            statement["text"] = fill_statement_variables(statement["text"], history)
            for property in statement.get("properties",[]):
                if ":" in property:
                    parts = property.split(":")

                    result = False

                    if parts[0] in handlers:
                        result = handlers[parts[0]](parts[1], previous_moves)
                    elif parts[0][:2] == "{{":
                        v = variable_manager.insert_values(auth_token, parts[0])
                        if v == parts[1]:
                            result = True
                    else:
                        result = False

                    if result:
                        properties_satisfied[i] = properties_satisfied[i] + 1
                        if properties_satisfied[i] > highest:
                            highest = properties_satisfied[i]
                    else:
                        properties_satisfied[i] = properties_satisfied[i] - 1

                    # negate = False
                    #
                    # if parts[1][0] == "!":
                    #     negate = True
                    #     parts[1] = parts[1][1:]
                    #
                    # if parts[0] == "previousmove" and parts[1] in previous_moves:
                    #     properties_satisfied[i] = properties_satisfied[i] + 1
                    #     if properties_satisfied[i] > highest:
                    #         highest = properties_satisfied[i]
                    # elif parts[0] == "lastmove" and len(previous_moves) > 0 and previous_moves[-1] == parts[1]:
                    #     properties_satisfied[i] = properties_satisfied[i] + 1
                    #     if properties_satisfied[i] > highest:
                    #         highest = properties_satisfied[i]
                    # else:
                    #     properties_satisfied[i] = properties_satisfied[i] - 1
                    #
                    #     print("{} is a previous move".format(parts[1]))
            i = i+1

        new_statements = [statements[i] for i in range(len(statements)) if properties_satisfied[i] == highest]
        print(new_statements)


        print(properties_satisfied)


        return new_statements
