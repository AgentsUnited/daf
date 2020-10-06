import daf
from daf import mongo
import activemq as internal

@daf.message_handler("DGEP/requests", "DGEP/response")
class DAFRequestHandler:

    def __init__(self):
        self.platform_topic = "<platform>/<topic>"

    @daf.command_handler("new")
    def handle_new_dialogue(self, command, data):
        """
        Handles a request for a new dialogue
        """
        topic = data.get("topic","").lower()
        username = data.get("username")


        if topic is None:
            return {"error":"Topic not specified"}
        elif username is None:
            return {"error":"Username not specified"}
        else:

            col = mongo.get_column("users")
            result = col.find_one({"username": username})

            if not result:
                return {"error":"User is not authenticated"}
            else:
                col = mongo.get_column("dialogue_topics")
                result = col.find_one({"topic": topic})

                if result:
                    platform = result["platform"].upper()
                    destination = platform + "/requests"

                    dialogueID = self.new_dialogue(platform, topic, username)

                    if dialogueID is not None:
                        data["dialogueID"] = dialogueID

                        if "participants" in data and platform == "UG":
                            new_participants = []
                            for p in data.get("participants"):
                                if p["player"] == "Agent" and p["name"] == "Olivia":
                                    p["player"] = "AgentOne"
                                elif p["player"] == "Agent" and p["name"] == "Emma":
                                    p["player"] = "AgentTwo"

                                new_participants.append(p)

                            data["participants"] = new_participants

                        internal.send_message(destination, {"cmd": command, "params": data}, self.headers)
                else:
                    return {"error":"Topic not found"}

    @daf.command_handler("moves")
    @daf.command_handler("interaction")
    @daf.command_handler(default=True)
    def handle_moves_interaction(self, command, data):
        """
        Handles requests for moves and sending interactions
        """
        dialogueID = data.get("dialogueID", None)

        if dialogueID is not None:
            platform = self.get_platform(dialogueID)
            if platform is not None:
                destination = platform + "/requests"
                internal.send_message(destination, {"cmd": command, "params": data}, self.headers)
        else:
            platform = data.get("platform", None)
            if platform is not None:
                destination = platform + "/requests"
                internal.send_message(destination, {"cmd": command, "params": data}, self.headers)



    def new_dialogue(self, platform, topic, username):
        """
        Create a new dialogue shell
        """
        dialogueID = int(mongo.get_record_count("dialogues")) + 1

        col = mongo.get_column("users")
        result = col.find_one({"username": username})

        if result:
            authToken = result["authToken"]

            data = {
                "dialogueID": dialogueID,
                "platform": platform,
                "topic": topic,
                "authToken": authToken,
                "dialogueData":{}
            }

            col = mongo.get_column("dialogues")
            col.insert_one(data)

            return dialogueID

        return None

    def get_platform(self, dialogueID):
        """
        Gets the platform for the dialogue with the given ID
        """
        col = mongo.get_column("dialogues")
        result = col.find_one({"dialogueID": dialogueID})

        if result:
            return result["platform"]
        else:
            return None
