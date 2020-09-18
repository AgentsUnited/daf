import daf
import dialogue
import user
from .moves import Moves

@daf.message_handler("UG/requests")
class Request:

    forward = "DGEP/requests"

    @daf.command_handler("new", forward_topic=forward)
    def new_request(self, command, data):
        """
        Handles a request sent with the 'new' command
        Tracks a new dialogue in the utterance generator
        """

        _user = user.get_user(data["username"])

        if _user is not None:
            auth_token = _user["authToken"]
        else:
            auth_token = None

        participants = data.get("participants", [])
        agents = {agent["name"]: agent for agent in participants if agent.get("type",None) == "agent"}

        data["sessionID"] = dialogue.new_dialogue(data.get("dialogueID", None),
                                      data["topic"],
                                      data.get("contentID", None),
                                      auth_token,
                                      agents)

        data["protocol"] = data["topic"].lower() # legacy

        return data

    @daf.command_handler("interaction", forward_topic=forward)
    @daf.command_handler("draftinteraction", forward_topic=forward)
    @daf.command_handler("moves", forward_topic=forward)
    @daf.command_handler("commit", forward_topic=forward)
    @daf.command_handler("protocols", forward_topic=forward)
    def default_request(self, command, data):
        """
        Default handler for requests that don't need the attention of the UG
        """
        print(data)
        return data
