from data.mongo import Mongo

class Participant:

    def __init(self)__:
        pass

    def add_participant(self, participant, auth_token):
        """ Method to add a participant to the DB
            The SKB auth token is used as a temporary identifier until
            DGEP sends back a dialogue ID

            :param participant JSON representation of the participant
            :auth_token SKB auth token
            :type participant json object
            :type auth_token string
            """

            print(participant)
            return

            participant["participant"] = coach["participant"].lower()
            participant["auth_token"] = auth_token
            participant["dialogueID"] = 0

            Mongo().insert(db="couch",
                           col="participant_specifications",
                           content=participant)
