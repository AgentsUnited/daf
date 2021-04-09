import daf
import json
import activemq as internal


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
                #internal.send_message(forward, {"cmd":command,"params":data}, self.headers)
                internal.send_message(forward, data, self.headers)

"""
Passthrough class can't be annotated because the topics its listens on depend
on the dynamic config file; so, we use the decorator functions directly to
create the listener based on the config.
"""
with open("/app/config.json") as config:
    config = json.load(config)
    for topic, data in config.items():
        if "forward" in data:
            daf.message_handler(topic, respond=False, accept="*")(Passthrough)()
            passthru[topic] = data["forward"]
