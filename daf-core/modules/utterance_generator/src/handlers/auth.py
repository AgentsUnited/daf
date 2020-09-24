import daf
from daf import mongo

@daf.message_handler("FILSTANTIATOR/auth")
class AuthHandler:

    @daf.command_handler("login")
    def login(self, command, data):
        username = data.get("username", None)
        authToken = data.get("authToken", None)

        if username is not None and authToken is not None:
            query = {"username": username}
            col = mongo.get_column("users")
            result = col.find_one(query)

            if result is None:
                col.insert_one(data)
            else:
                col.update(query, {"$set": {"authToken": authToken}})

    @daf.command_handler("logout")
    def logout(self, data):
        username = data.get("username", None)

        query = {"username": username}
        result = col.find_one(query)

        if result:
            col.delete_one(query)
