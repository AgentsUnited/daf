import daf

@daf.message_handler("DGEP/requests", "DGEP/response")
class DGEPRequestHandler:

    @daf.command_handler("new")
    def new_dgep_dialogue(self, command, data):

        if topic in data:
            topic = data["topic"].lower()




        return

    @daf.command_handler("interaction", response_topic="DGEP/moves")
    def dgdp_interaction(self, command, data):
        return
