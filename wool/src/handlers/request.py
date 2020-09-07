import daf
import requests
import json

_user_data = {}
_dialogue_data = {}

@daf.message_handler("WOOL/requests", "WOOL/response")
@daf.message_handler("WOOL/auth", None)
class WoolRequestHandler:

    def __init__(self):
        self.server = "https://servletstest.rrdweb.nl/wool/v1/dialogue/"
        self.actions = ["start-dialogue", "progress-dialogue", "cancel-dialogue"]

    @daf.command_handler("login")
    def handle_login(self, command, data):
        username = data.get("username", None)
        authToken = data.get("authToken", None)

        if username is not None and authToken is not None:
            _user_data[username] = {"authToken": authToken}

        return data

    @daf.command_handler("new")
    def handle_new(self, command, data):
        dialogueID = data.get("dialogueID", None)
        username = data.get("username", None)
        topic = data.get("topic", None)
        participants = data.get("participants", None)

        if dialogueID is not None and username is not None and topic is not None and participants is not None:

            _dialogue_data[dialogueID] = {"authToken": _user_data[username]["authToken"]}
            _dialogue_data[dialogueID]["participants"] = {p["player"].lower(): p["name"] for p in participants}
            _dialogue_data[dialogueID]["moveData"] = self.start_dialogue(dialogueID)

            response = {"dialogueID": dialogueID,
                        "moves": self.handle_moves("moves", data),
                        "participants": participants,
                        "clearvars": []
            }

            return response

        return {}

    @daf.command_handler("moves", response_topic="WOOL/dialogue_moves")
    def handle_moves(self, command, data):
        dialogueID = data.get("dialogueID", None)

        if dialogueID is not None:
            return {"status":"active","dialogueID": dialogueID, "moves": _dialogue_data[dialogueID]["moveData"]["moves"]}
        else:
            return {}

    @daf.command_handler("interaction")
    def handle_interaction(self, command, data):
        dialogueID = data.get("dialogueID", None)

        to_return = {"moves": {}}

        if dialogueID is not None:
            dialogue_data = _dialogue_data[dialogueID]["moveData"]
            if data["moveID"].lower() == "agentmove":
                # are there any replies
                if dialogue_data["replies"]:
                    user = _dialogue_data[dialogueID]["participants"]["user"]
                    _dialogue_data[dialogueID]["moveData"]["moves"] = {user: []}

                    for reply in dialogue_data["replies"]:
                        move = {"moveID": str(reply["replyId"]), "target":"", "reply":{}, "opener": " ".join([s["text"] for s in reply["statement"]["segments"]])}
                        _dialogue_data[dialogueID]["moveData"]["moves"][user] = move
                else:
                    response = self.progress_dialogue(dialogueID, "1")
                    if response is not None:
                        _dialogue_data[dialogueID]["moveData"] = response

            else:
                # need to advance the dialogue
                response = self.progress_dialogue(dialogueID, data["moveID"])
                if response is not None:
                    _dialogue_data[dialogueID]["moveData"] = response


        return self.handle_moves("moves", data)

    def wool_request(self, dialogueID, action, post_data=None, qs=None):

        queryString = ""

        if qs is not None:
            queryString = "?" + "&".join([k + "=" + v for k,v in qs.items()])

        authToken = _dialogue_data[dialogueID]["authToken"]

        if authToken is not None and action in self.actions:
            url = self.server + action + queryString

            headers = {"content-type": "application/json", "accept": "*/*", "X-Auth-Token": authToken}
            response = requests.post(url, headers=headers)
            return json.loads(response.text)
        else:
            return None

    def start_dialogue(self, dialogueID):
        to_return = {"moves": {}, "replies": []}
        response = self.wool_request(dialogueID, "start-dialogue", qs={"dialogueName": "carlos-social-introduction", "language":"en"})
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

    def progress_dialogue(self, dialogueID, moveID):
        to_return = {"moves": {}, "replies": []}
        response = self.wool_request(dialogueID, "progress-dialogue", qs={"replyId": moveID})
        if response is not None:
            opener = " ".join([s["text"] for s in response["value"]["statement"]["segments"]])
            to_return["moves"][response["value"]["speaker"]] = [{"moveID": "AgentMove", "target":"", "reply":{}, "opener": opener}]


            replies = True

            for r in response["value"]["replies"]:
                if r["statement"] is None:
                    replies = False
                    break

            if replies:
                to_return["replies"] = response["value"]["replies"]

        return to_return
