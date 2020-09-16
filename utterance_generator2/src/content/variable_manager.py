import re
import requests
import os
import json
import mongo

_content_location = "https://servletstest.rrdweb.nl/wool/v1" #os.getenv('CONTENT_DATABASE')

def get_values(auth_token, variables):
    """
    Get the values for the given variables from the WOOL variable store
    """
    to_return = {}

    headers = {
        "content-type": "application/json",
        "accept": "*/*",
        "X-Auth-Token": auth_token
    }

    query_string = requests.utils.quote(" ".join(variables))
    response = requests.get(_content_location + "/variables?names=" + query_string, headers=headers)
    to_return = json.loads(response.text)

    return to_return

def get_value(auth_token, variable):
    """
    Gets the value of the given variable
    """
    values = get_values(auth_token, [variable])
    return values.get(variable, None)


def get_terms(auth_token, variables):
    """
    Gets values for the given variables and returns as variable(value) terms
    """
    terms = []
    values = get_values(auth_token, variables)

    for key, value in values.items():
        if value is None:
            continue
        if type(value) is list:
            for v in value:
                terms.append("{}({})".format(key, v))
        else:
            terms.append("{}({})".format(key, value))

    return terms


def insert_values(auth_token, input):
    """
    Replaces any {{instances}} with values from the variable store, if
    they exist
    """

    matches = re.findall(re.compile(r"(?:{{([^{}]+)}})"), input)

    if matches:
        for m in matches:
            value = get_value(auth_token, m)
            if value is not None:
                input = input.replace("{{{{{var}}}}}".format(var=m), value)

    return input

def get_clear_vars(topic):
    """
    Gets the "clearvars" for the given topic, variables that should be cleared
    when a new dialogue is started using that topic
    """
    to_return = []

    col = mongo.get_column("variables")
    result = col.find({"topic": topic})

    if result:
        for r in result:
            if "variables" in r:
                for move_name, variables in r["variables"].items():
                    for name, parameters in variables.items():
                        if parameters.get("clear_on_new",False) == True:
                            to_return.append(name)

    return to_return


def evaluate_value(auth_token, expr):
    """
    Determines the value based on a '[]' expression
    """

    regex = r"\[([^=!]+)(!?=)(.*)\?([^:]+)(?::(.*))?\]"

    matches = re.findall(regex, expr)

    if matches:
        expression = matches[0][0]
        comparison = matches[0][1]
        value = matches[0][2]
        if_true = matches[0][3]
        if len(matches[0]) > 4:
            if_false = matches[0][4]
        else:
            if_false = ""

        expression = insert_values(auth_token, expression)

        if comparison == "=":
            negate = False
        else:
            negate = True

        if expression == value and not negate:
            return if_true
        else:
            return if_false

    return ""

def get_move_vars(topic, move_name, reply, auth_token=None):
    """
    Gets the variables that the given move in the given topic should store,
    then adds values based on the reply (if required)
    """
    to_return = {}

    col = mongo.get_column("variables")
    result = col.find({"topic": topic})

    if result is not None:
        for r in result:
            if "variables" in r:
                for name, var in r["variables"].get(move_name, {}).items():
                    value = var.get("value","")
                    if auth_token is not None:
                        name = insert_values(auth_token, name)

                    append = False
                    if "append" in var and type(var["append"]) == bool:
                        append = var["append"]

                    if type(value) is str:

                        if value[0] == "[" and value[-1] == "]":
                            value = evaluate_value(auth_token, value)

                        if value[0] == "$":
                            if value[1:] in reply:
                                value = reply[value[1:]]

                                matches = re.findall(re.compile(r"(?:[^() ])+\(([^()]+)\)"), value)
                                if matches:
                                    value = matches[0]
                            else:
                                value = ""

                    to_return[name] = {"append": append, "value": value}

    return to_return
