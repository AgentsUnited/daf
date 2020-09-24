import daf
from daf import mongo

# protected mongodb collections
_protected = ["dialogues"]

@daf.message_handler("DGEP/content")
class ContentHandler:

    @daf.command_handler("create")
    def create_content(self, command, data):
        """
        Create content in the DAF
        The "data" field should be in the form:
        {"type":str,"content":{}}
        """

        type = data.get("type", None)

        if type is not None and type not in _protected:
            col = mongo.get_column(type)
            content = data.get("content",{})
            col.insert_one(content)
            return {"status":"OK"}
        else:
            return {"status":"error", "message":"Invalid 'type'"}

    @daf.command_handler("export")
    def export_content(self, command, data):
        """
        Export content from the DAF
        The "data" field should be in the form:
        {"type":str,"query":{}}
        where "query" is a mongodb style query
        """

        if "type" in data:
            col = mongo.get_column(data["type"])
            query = data.get("query",{})

            if type(query) is dict:
                result = col.find(query, {"_id": False})

                if result:
                    return {"content": list(result)}

        return {}
