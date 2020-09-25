import daf
from daf import mongo

@daf.message_handler("COUCH/USER/AUTHENTICATION",respond=False)
class DAFAuthHandler:

    @daf.command_handler("login")
    def login(self, command, data):
        username = data.get("username", None)
        authToken = data.get("authToken", None)

        if username is not None and authToken is not None:
            col = mongo.get_column("users")
            col.insert_one({"username": username, "authToken": authToken})

    @daf.command_handler("logout")
    def logout(self, command, data):
        username = data.get("username")

        if username is not None:
            col = mongo.get_column("users")
            col.delete_one({"username": username})
