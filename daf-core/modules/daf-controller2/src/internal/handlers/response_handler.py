import daf
import activemq as external

class ResponseHandler:

    def __init__(self):
        pass

    @daf.command_handler("new")
    @daf.command_handler(default=True)
    def handle_new(self, command, data):
        destination = "DGEP/response"
        external.send_message(destination, data)

    @daf.command_handler("moves")
    @daf.command_handler("interaction")
    def handle_returned_moves(self, command, data):
        destination = "DGEP/moves"
        external.send_message(destination, data)
