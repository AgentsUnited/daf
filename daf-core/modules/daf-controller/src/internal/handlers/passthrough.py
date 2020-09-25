import json
import daf
import activemq as external

passthru = {}

class Passthrough:
    """
    Special class to handle "passthrough" messages, those messages that deal with
    functionality provided to individual modules.
    """

    @daf.command_handler(default=True)
    def default(self, command, data):
        if self.destination is not None:
            forward = passthru.get(self.destination, None)

            if forward is not None:
                external.send_message(forward, {"cmd":command,"params":data}, self.headers)


# we also need to listen to response topics for passthrough messages
with open("config.json", "r") as config:
    config = json.load(config)

    for topic, data in config.items():
        if "response" in data and data["response"] != "":
            response_topic = data["response"]
        else:
            response_topic = data["forward"] + "/response"

        passthru[response_topic] = topic + "/response"
        daf.message_handler(response_topic, respond=False)(Passthrough)()
