import daf
import uuid
from daf import mongo

@daf.message_handler("utterance_generator/content")
class Content:
    """
    Handles the creation, import and export of content
    """

    response = "utterance_generator/response"

    @daf.command_handler("new")
    def new_content(self, command, data):
        return "new content"

    @daf.command_handler("import")
    def import_content(self, data):
        return "import content"

    @daf.command_handler("export")
    def export_content(self, data):
        return "export content"
