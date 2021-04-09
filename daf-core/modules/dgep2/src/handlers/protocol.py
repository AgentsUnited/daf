import daf
from daf import mongo
import dgdl

@daf.message_handler("DGEP/protocol", "DGEP/response", accept="dgdl")
class Protocol:

    """
    Accepts and stores DGDL specifications
    """

    @daf.command_handler(default=True)
    def accept_dgdl(self, command, data):
        """
        Accept the given dgdl (data) and store it
        """
        parser = dgdl.DGDLParser()
        game = parser.parse(input=data)

        self.headers["type"] = "json"

        if(isinstance(game, list)):
            return {"response":"error","errors": game}
        else:
            gameID = game.gameID

            col = mongo.get_column("dgdl_files")
            col.update({"gameID": gameID}, {"dgdl": data}, upsert=True)

            print("Game ID: " + game.gameID)
            return {"response":"OK"}
