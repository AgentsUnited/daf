import requests
import json
import os
import pymongo
import re

class SKB:
    """
    Class to connect to a shared knowledge base (SKB) and retreive variable values

    Attributes:
        auth_token (str): the auth token to login with

    """
    #  eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0MDAxQGNvdW5jaWwtb2YtY29hY2hlcy5ldSIsImlhdCI6MTU4NzcxNTk3MH0._DA5oO1O6hqV_45xiroUeeU2tYykawxBt8WFFm7njO2AQJVZRlzjFJIblRJmvv0YULAFgoaM_vuAQs-MC6YORw

    def __init__(self, auth_token=None, dialogueID=None):
        self.server = os.getenv('CONTENT_DATABASE')
        self.standard_headers = {'content-type': 'application/json', 'accept': '*/*'}

        self.variable_regex = re.compile(r"{([^{}]+)}")

        auth_token="eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0MDAxQGNvdW5jaWwtb2YtY29hY2hlcy5ldSIsImlhdCI6MTU5NjIyOTgwNn0.0OLdmIET4QBqk2nt970dFXx_ki8DikHT1_JjQoAnKwBGg5fna__g4Sg4cH1b2kGdQBzMofhjH7LwnJ0odEXFZg"

        if auth_token is None:
            if dialogueID is None:
                #self.mock_login()
                print("Unable to use SKB")
            else:
                self.auth_token = self.get_auth_token_for_dialogue(dialogueID)
                if self.auth_token is None:
                    print("Unable to use SKB")
        else:
            self.auth_token = auth_token

        print("Auth token: " + str(self.auth_token))

    def get_auth_token_for_dialogue(self, dialogueID):
        """ Method to get the auth token for the current dialogueID """

        db_name = os.getenv("MONGODB")
        mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
        col = mongo[db_name]["users"]

        result = col.find_one({"dialogueID": dialogueID})

        if result is not None:
            return result["authToken"]
        else:
            return None

    def get_variable_value(self, var_name):
        """ Method to get the value of a single variable in the SKB """

        return self.get_variable_values([var_name])

    def get_variable_values(self, var_names):
        """ Method to get the values of the given variables in the SKB """

        if self.auth_token is None:

            db_name = os.getenv("MONGODB")
            mongo = pymongo.MongoClient("mongodb://mongodb:27017/")
            col = mongo[db_name]["coaching_variables"]

            result = col.find_one()

            to_return = {key: value for (key, value) in result.items() if key in var_names}

            return to_return
        else:
            headers = self.standard_headers
            headers["X-Auth-Token"] = self.auth_token

            query_string = requests.utils.quote(" ".join(var_names))
            response = requests.get(self.server + "/variables?names=" + query_string, headers=headers)

            variables = json.loads(response.text)

            to_return = {}

            for key,value in variables.items():
                if value is not None or value != "":
                    to_return[key] = value

            return to_return

    def fill_skb_variables(self, input):
        '''
        Fills any {string} pattern with the value of string in the skb
        '''
        matches = re.findall(self.variable_regex, input)

        if matches:
            values = self.get_variable_values(matches)

            for k,v in values.items():
                input = input.replace("{" + k + "}", str(v))
        return input



    def mock_login(self):
        """
        Method to mock a login when an auth key isn't provided

        Should only be used in testing
        """

        print("SKB: no auth token found; performing mock login")
        request = json.dumps({'password': 'beqewymoh', 'tokenExpiration': 'never', 'user': 'test001@council-of-coaches.eu'})
        headers = self.standard_headers
        response = requests.post(self.server + "/auth/login", data = request, headers = headers)

        try:
            response = json.loads(response.text)
            self.auth_token = response["token"]
        except:
            print("SKB: Error logging in to SKB")
            self.auth_token = None
