import daf
from daf import mongo
import uuid
from dgep import Dialogue as DGEP
import dgdl

@daf.message_handler("DGEP/requests","DGEP/response")
class DGEPRequestHandler:

    """
    Handles messages sent to the DGEP/requests topic
    """

    def __init__(self):
        pass

    @daf.command_handler("new")
    def handle_new(self, command, data):
        """
        Handles "new" commands by creating a new dialogue
        """

        print("Received message")

        response = {}

        if "topic" in data:
            protocol = data["topic"].lower()
            dialogueID = data.get("dialogueID", None)

            f = open("/app/goalsetting.dgdl");

            dgdl = f.read();

            #TODO: yarn translation
            dgep = DGEP()
            dialogue = dgep.new_dialogue(dgdl, **data)

            # save in mongodb
            dialogueID = self.save_dialogue(dialogue, dialogueID)

            moves = dgep.get_available_moves()

            response["dialogueID"] = dialogueID
            response["moves"] = moves
            response["history"] = []

        return response


    @daf.command_handler("moves", response_topic="DGEP/moves")
    def handle_moves(self, command, data):

        response = {}

        if "dialogueID" in data:
            dialogueID = data["dialogueID"]
            dialogue = self.load_dialogue(dialogueID)

            response = {
                "dialogueID": dialogueID,
                "status": dialogue.status,
                "moves": dialogue.get_available_moves(),
                "history": dialogue.dialogue_history
            }

        return response

    @daf.command_handler("interaction", response_topic="DGEP/moves")
    def handle_interaction(self, command, data):
        response = {}

        if "dialogueID" in data and "interactionID" in data:
            dialogueID = data["dialogueID"]
            dialogue = self.load_dialogue(dialogueID)

            response = {
                "dialogueID": dialogueID,
                "status": dialogue.status,
                "moves": dialogue.perform_interaction(**data),
                "history": dialogue.dialogue_history
            }

            self.save_dialogue(dialogue.save(), dialogueID)

        return response

    @daf.command_handler("draftinteraction", response_topic="DGEP/moves")
    def handle_draft_interaction(self, command, data):
        """
        Performs a draft interaction - the any changes are only saved as
        draft and will only affect the dialogue if subsequently committed
        """
        response = {}

        if "dialogueID" in data and "interactionID" in data:
            dialogueID = data["dialogueID"]
            dialogue = self.load_dialogue(dialogueID)

            response = {
                "dialogueID": dialogueID,
                "status": dialogue.status,
                "moves": dialogue.perform_interaction(**data),
                "history": dialogue.dialogue_history
            }

            self.save_dialogue(dialogue.save(), dialogueID, True)

        return response

    @daf.command_handler("commit", response_topic="DGEP/moves")
    def handle_commit(self, command, data):
        """
        Commits a previous draft interaction
        """
        response = {}

        if "dialogueID" in data:
            dialogueID = data["dialogueID"]

            dialogue = self.load_dialogue(dialogueID, True)

            if dialogue is not None:
                response = {
                    "dialogueID": dialogueID,
                    "status": dialogue.status,
                    "moves": dialogue.get_available_moves(),
                    "history": dialogue.dialogue_history
                }

                self.save_dialogue(dialogue.save(), dialogueID)

        return response

    def save_dialogue(self, dialogue, dialogueID=None, draft=False):
        """
        Save the given dialogue with the given dialogueID
        Also clears any draft saving if draft = False

        :param dialogue the DGEP (Dialogue) object to save
        :param dialogueID the dialogueID to save at
        :param draft only save a draft version of the dialogue
        """
        col = mongo.get_column("dialogues")

        if dialogueID is not None:
            field = "dialogueData.dgep" if not draft else "dialogueData.dgep_draft"
            query = {"dialogueID": dialogueID}
            dialogue_data = {"$set": {field: dialogue}}
            col.update_one(query, dialogue_data)

            # clear any draft data
            if not draft:
                clear_draft = {"$set":{"dialogueData.dgep_draft": None}}
                col.update_one(query, clear_draft)

        return dialogueID

    def load_dialogue(self, dialogueID, draft=False):
        """
        Load a dialogue with the given dialogueID

        :param dialogueID: the dialogue ID to load
        :type dialogueID: str
        :return: the loaded dialogue
        :rtype: DGEP (Dialogue) instance
        """
        col = mongo.get_column("dialogues")

        if dialogueID is not None:

            field = "dgep" if not draft else "dgep_draft"

            query = {"dialogueID": dialogueID}
            result = col.find_one({"dialogueID": dialogueID})
            return DGEP(result["dialogueData"][field])
        else:
            return None
