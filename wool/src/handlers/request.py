import daf
import requests
import json
import mongo

@daf.message_handler("WOOL/requests", "WOOL/response")
class WoolRequestHandler:

    def __init__(self):
        self.server = "https://servletstest.rrdweb.nl/wool/v1/dialogue/"
        self.actions = ["start-dialogue", "progress-dialogue", "cancel-dialogue"]
        self.dialogue = {}

    @daf.command_handler("new")
    def handle_new(self, command, data):
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

            if authToken is None:
                return {"error": "User is not authorised"}

            self.dialogue = {
                "source": "wool",
                "dialogueID": dialogueID,
                "authToken": authToken,
                "participants": {p["player"].lower(): p["name"] for p in participants}
            }
            self.dialogue["moveData"] = self.start_dialogue()
            self.save_dialogue()

            response = {"dialogueID": dialogueID,
                        "moves": self.dialogue["moveData"]["moves"],
                        "participants": participants,
                        "clearvars": []
            }

            return response

        return {}

    @daf.command_handler("moves", response_topic="WOOL/dialogue_moves")
    def handle_moves(self, command, data):
        dialogueID = data.get("dialogueID", None)
        self.dialogue = self.load_dialogue(dialogueID)

        if dialogueID is not None:
            return {"status":"active","dialogueID": dialogueID, "moves": self.dialogue["moveData"]["moves"]}
        else:
            return {}

    @daf.command_handler("interaction")
    def handle_interaction(self, command, data):
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
                    response = self.progress_dialogue(dialogueID, "1")
                    if response is not None:
                        self.dialogue["moveData"] = response

            else:
                # need to advance the dialogue
                response = self.progress_dialogue(dialogueID, data["moveID"])
                if response is not None:
                    self.dialogue["moveData"] = response

        self.save_dialogue()

        return self.handle_moves("moves", data)

    def load_dialogue(self, dialogueID):
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
        queryString = ""

        if qs is not None:
            queryString = "?" + "&".join([k + "=" + v for k,v in qs.items()])

        authToken = self.dialogue.get("authToken", None)

        if authToken is not None and action in self.actions:
            url = self.server + action + queryString

            headers = {"content-type": "application/json", "accept": "*/*", "X-Auth-Token": authToken}
            response = requests.post(url, headers=headers)
            return json.loads(response.text)
        else:
            return None

    def start_dialogue(self):
        response = self.wool_request("start-dialogue", qs={"dialogueName": "carlos-social-introduction", "language":"en"})
        return self.get_moves_from_response(response)

    def progress_dialogue(self, dialogueID, moveID):
        response = self.wool_request("progress-dialogue", qs={"replyId": moveID})
        return self.get_moves_from_response(response["value"])

    def get_moves_from_response(self, response):
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
