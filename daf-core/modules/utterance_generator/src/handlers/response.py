import daf
import dialogue
from content import variable_manager
from handlers.moves import Moves

@daf.message_handler("DGEP/response", "UG/response")
class Response:

    @daf.command_handler("new")
    def handle_response(self, command, data):
        dialogue_id = data.get("dialogueID", None)
        session_id = data.get("sessionID", None)

        if dialogue_id is not None and session_id is not None:
            dialogue.set_dialogue_id(session_id, dialogue_id)

            data = Moves().handle_moves(command, data)
            data["clearvars"] = variable_manager.get_clear_vars(dialogue.get_auth_token(dialogue_id), dialogue.get_topic(dialogue_id))

        return data

    @daf.command_handler(default=True)
    def handle_default(self, command, data):
        return data
