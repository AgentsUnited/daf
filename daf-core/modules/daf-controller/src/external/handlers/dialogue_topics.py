import daf
from daf import mongo

@daf.message_handler("DGEP/dialogue_topics")
class DialogueTopicsHandler:
    """
    Handler for the creation and management of topics
    Topics are mapped to dialogue management platforms
    """

    @daf.command_handler("new")
    def handle_new(self, command, data):
        topic = data.get("topic", None)
        platform = data.get("platform", None)

        to_return = {}

        if topic is not None and platform is not None:
            col = mongo.get_column("dialogue_topics")
            col.insert_one(data)

            to_return["status"] = "OK"
        else:
            to_return["status"] = "error"
            to_return["message"] = "'topic' and 'platform' required"

        return to_return

    @daf.command_handler("list")
    def handle_new(self, command, data):
        if "platform" in data:
            query = {"platform": data.get("platform")}
        else:
            query = {}

        to_return = []

        col = mongo.get_column("dialogue_topics")
        result = col.find(query, {"_id": False})

        if result:
            to_return = [r for r in result]

        return to_return
