import daf
import dialogue
import mongo
from content import Statement, content_locator, variable_manager

@daf.message_handler("DGEP/moves", "FILSTANTIATOR/dialogue_moves")
class Moves:

    @daf.command_handler("moves")
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
                print("Descriptors")
                print(descriptors)
                if descriptors is not None:
                    if self.move_requires_content(move):
                        if "content" in descriptors:
                            content = content_locator.find_content(dialogue_id, speaker, descriptors["content"],move)

                            for c in content:
                                new_reply = {}

                                for key, value in move.get("reply",{}).items():
                                    if key not in c["content"]:
                                        new_reply[key] = value

                                new_reply.update(c["content"])

                                variables = variable_manager.get_move_vars(dialogue.get_topic(dialogue_id), move_id, new_reply, dialogue.get_auth_token(dialogue_id))

                                for statement in self.filter_statements(c["statements"]):
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
                        for statement in self.filter_statements(statements):
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

        col = mongo.get_column("content_descriptors")
        result = col.find_one({"protocol": topic})

        if result is not None:
            if move_id in result["descriptors"]:
                return result["descriptors"][move_id]

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

    def filter_statements(self, statements):
        """
        TODO: various filtering methods for statements based on properties
        """
        return statements
