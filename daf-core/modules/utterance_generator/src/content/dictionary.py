from daf import mongo
import dialogue
from content import term, variable_manager

def get_entry(dialogue_id, entry, parameters=None):
    """
    Get an entry from the dictionary for the given statement
    """

    content_id = dialogue.get_content_id(dialogue_id)

    to_return = []
    if parameters is None:
        parameters = []

    dictionary = {}
    auth_token = dialogue.get_auth_token(dialogue_id)

    result = mongo.get_column("dictionary").find({"contentID": content_id})

    if result:
        for r in result:
            for key, value in r.get("entries", {}).items():
                _term = term.get_term_specification(key)
                t = variable_manager.insert_values(auth_token, _term[0])
                dictionary[t] = {"variables": _term[2], "statements": value}

    if entry in dictionary:
        entry = dictionary[entry]

        variables = entry["variables"]
        mapping = dict(zip(variables, parameters))

        # give default values to parameters not assigned
        mapping.update({a: a for a in variables if a not in mapping})

        for statement in entry.get("statements", []):
            text = statement["text"]
            for key,value in mapping.items():
                text = text.replace("${}".format(key), value)

            text = variable_manager.insert_values(auth_token, text)

            to_return.append({"text": text, "properties": statement["properties"]})

    return to_return
