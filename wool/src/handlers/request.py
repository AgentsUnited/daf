import daf
import requests
import json
import mongo

@daf.message_handler("WOOL/requests", "WOOL/response")
class WoolRequestHandler:
    """
    Handles messages sent to the WOOL/requests topic
    """

    def __init__(self):
        self.server = "https://servletstest.rrdweb.nl/wool/v1/dialogue/"
        self.actions = ["start-dialogue", "progress-dialogue", "cancel-dialogue"]
        self.dialogue = {}

    @daf.command_handler("new")
    def handle_new(self, command, data):
        """
        Handle "new" commands
        """
        dialogueID = data.get("dialogueID", None)
        username = data.get("username", None)
        topic = data.get("topic", None)
        participants = data.get("participants", None)

        col = mongo.get_column("users")
        user_data = col.find_one({"username": username})

        if user_data is None:
            return {"error":"user is not authorised"}

        if dialogueID is not None and username is not None and topic is not None and participants is not None:
            authToken = user_data.get("authToken", None)

            # get the "agent" participant
            agent = None

            for p in participants:
                if p["player"].lower() == "agent":
                    agent = p["name"].lower()
                    break

            if authToken is None or agent is None:
                return {"error": "User is not authorised"}

            participants_new = []

            i = 1
            for p in participants:
                participants_new.append({"name": p["name"], "participantID": i})
                i = i+1


            self.dialogue = {
                "source": "wool",
                "dialogueID": dialogueID,
                "authToken": authToken,
                "participants": {p["player"].lower(): p["name"] for p in participants}
            }
            move_data = self.start_dialogue(topic, agent)

            if move_data is None:
                return {}

            self.dialogue["moveData"] = move_data
            self.save_dialogue()

            response = {"dialogueID": dialogueID,
                        "moves": self.dialogue["moveData"]["moves"],
                        "participants": participants_new,
                        "clearvars": []
            }

            return response

        return {}

    @daf.command_handler("moves", response_topic="WOOL/dialogue_moves")
    def handle_moves(self, command, data):
        """
        Handle "moves" command, overriding the response topic to be WOOL/dialogue_moves
        """
        dialogueID = data.get("dialogueID", None)
        self.dialogue = self.load_dialogue(dialogueID)

        if dialogueID is not None:
            return {"status":"active","dialogueID": dialogueID, "moves": self.dialogue["moveData"]["moves"]}
        else:
            return {}

    @daf.command_handler("interaction", response_topic="WOOL/dialogue_moves")
    def handle_interaction(self, command, data):
        """
        Handle "interaction" command
        """
        dialogueID = data.get("dialogueID", None)

        to_return = {"moves": {}}

        if dialogueID is not None:
            self.dialogue = self.load_dialogue(dialogueID)
            to_return["dialogueID"] = dialogueID

            if self.dialogue is None:
                return to_return

            dialogue_data = self.dialogue["moveData"]
            if data["moveID"].lower() == "agentmove":
                # are there any replies
                if dialogue_data["replies"]:
                    user = self.dialogue["participants"]["user"]
                    self.dialogue["moveData"]["moves"] = {user: []}

                    for reply in dialogue_data["replies"]:
                        move = {"moveID": str(reply["replyId"]), "target":"", "reply":{}, "opener": " ".join([s["text"] for s in reply["statement"]["segments"]])}
                        self.dialogue["moveData"]["moves"][user] = move
                else:
                    response = self.progress_dialogue("1")
                    if response is not None:
                        self.dialogue["moveData"] = response

            else:
                # need to advance the dialogue
                response = self.progress_dialogue(data["moveID"])
                if response is not None:
                    self.dialogue["moveData"] = response

        self.save_dialogue()

        return self.handle_moves("moves", data)

    def load_dialogue(self, dialogueID):
        """
        Load a dialogue with the given dialogueID

        :param dialogueID: the dialogue ID to load
        :type dialogueID: str
        :return: the loaded dialogue
        :rtype: dict
        """
        if dialogueID is None:
            self.dialogue = {}
        else:
            col = mongo.get_column("dialogues")
            result = col.find_one({"dialogueID": dialogueID})
            self.dialogue = result
        return self.dialogue

    def save_dialogue(self):
        dialogueID = self.dialogue["dialogueID"]

        col = mongo.get_column("dialogues")
        result = col.replace_one({"dialogueID": dialogueID}, self.dialogue, upsert=True)

    def wool_request(self, action, post_data=None, qs=None):
        """
        Send a request to the Wool Web Service

        :param action: the action to perform
        :param post_data: optional post data to send to the action
        :param qs optional query string parameters and values
        :type action: str
        :type post_data: dict
        :type qs: dict
        :return: the response from the request, or None on failure
        :rtype: dict, or None on failure
        """
        queryString = ""

        if qs is not None:
            queryString = "?" + "&".join([k + "=" + v for k,v in qs.items()])

        authToken = self.dialogue.get("authToken", None)

        if authToken is not None and action in self.actions:
            url = self.server + action + queryString

            headers = {"content-type": "application/json", "accept": "*/*", "X-Auth-Token": authToken}
            response = requests.post(url, headers=headers)

            if response.status_code == 200:
                return json.loads(response.text)
            else:
                return None
        else:
            return None

    def start_dialogue(self, topic, agent):
        """
        Start a dialogue in the Wool Web Service

        :param topic: the topic of the dialogue
        :param agent: the name of the agent in the dialogue
        :type topic: str
        :type agent: str
        :return: the moves available
        :rtype: dict
        """

        # TODO: take topic and agent and select dialogue

        response = self.wool_request("start-dialogue", qs={"dialogueName": "carlos-social-introduction", "language":"en"})

        if response is not None:
            return self.get_moves_from_response(response)
        else:
            return None

    def progress_dialogue(self, moveID):
        """
        Progress the dialogue based on playing the given moveID

        :param moveID: the ID of the move
        :type moveID: int
        :return: the moves available
        :rtype: dict
        """
        response = self.wool_request("progress-dialogue", qs={"replyId": moveID})
        return self.get_moves_from_response(response["value"])

    def get_moves_from_response(self, response):
        """
        Gets the set of moves from a Wool response

        :param response: the response from Wool
        :type response: dict
        :return: the moves
        :rtype: dict
        """
        to_return = {"moves": {}, "replies": []}

        if response is not None:
            opener = " ".join([s["text"] for s in response["statement"]["segments"]])
            to_return["moves"][response["speaker"]] = [{"moveID": "AgentMove", "target":"", "reply":{}, "opener": opener}]

            replies = True

            for r in response["replies"]:
                if r["statement"] is None:
                    replies = False
                    break

            if replies:
                to_return["replies"] = response["replies"]

        return to_return
