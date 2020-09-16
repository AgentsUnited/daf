import daf
import mongo

@daf.message_handler("DGEP/content")
class ContentHandler:

    @daf.command_handler("create")
    def create_content(self, command, data):
        """
        Create content in the DAF
        The "data" field should be in the form:
        {"type":str,"content":{}}
        """

        if "type" in data:
            col = mongo.get_column(data["type"])
            content = data.get("content",{})
            col.insert_one(content)
            return {}
        else:
            return {"error":"'type' not specified"}

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
