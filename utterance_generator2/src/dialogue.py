import uuid
import mongo

"""
Module to handle dialogue tracking in the utterance generator
"""

def new_dialogue(topic, content=None, auth_token=None, agents=None):
    """
    Track a new dialogue, generating a temporary session ID
    """
    if agents is None:
        agents = {}

    session_id = str(uuid.uuid4())

    dialogue = {
        "sessionID": session_id,
        "topic": topic.lower(),
        "content": content,
        "authToken": auth_token,
        "agents": agents
    }

    col = mongo.get_column("dialogues")
    col.insert_one(dialogue)

    return session_id

def set_dialogue_id(session_id, dialogue_id):
    """
    Set the DGEP dialogue ID for the dialogue with the given session ID
    """
    col = mongo.get_column("dialogues")

    result = col.update_one({"sessionID":session_id},{"$set":{"dialogueID": dialogue_id}})

def get_dialogue(dialogue_id):
    """
    Get the dialogue with the given ID
    """
    col = mongo.get_column("dialogues")
    return col.find_one({"dialogueID": dialogue_id})

def get_topic(dialogue_id):
    """
    Gets the topic for the given dialogue
    A frequent use case so is essentially a shortcut to getting the dialogue
    then extracting the topic
    """
    print("Finding the topic for dialogueID: " + str(dialogue_id))
    dialogue = get_dialogue(dialogue_id)
    if dialogue is not None:
        return dialogue["topic"]

def get_auth_token(dialogue_id):
    """
    Gets the auth token for the given dialogue
    """
    dialogue = get_dialogue(dialogue_id)
    if dialogue is not None:
        return dialogue["authToken"]

def get_content_id(dialogue_id):
    """
    Gets the content ID for the given dialogue
    """
    return "abc"
    # dialogue = get_dialogue(dialogue_id)
    # if dialogue is not None:
    #     return dialogue["content"]
