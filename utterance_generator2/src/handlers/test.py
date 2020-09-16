import daf
import dialogue

@daf.message_handler("UG/test")
class TestHandler:
    """
    Class to accept messages for testing purposes
    """

    @daf.command_handler("variables")
    def handle_test_variables(self, command, data):
        from content import variable_manager

        dialogueID = data.get("dialogueID", None)

        if dialogueID is not None:
            authToken = dialogue.get_auth_token(dialogueID)

            expr = data.get("expr", "[{{userGender}}=male?shortTerm:longTerm]")

            print(variable_manager.evaluate_value(authToken, expr))
