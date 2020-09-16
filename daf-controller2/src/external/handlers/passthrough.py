import daf
import json
import activemq as internal


passthru = {}


class Passthrough:

    def default(self, command, data):
        if self.destination is not None:
            config = passthru.get(self.destination,{})

            if command in config:
                internal.send_message(config[command],{"cmd":command,"params":data})

with open("/app/config.json") as config:
    config = json.load(config)
    for topic, handler in config.items():
        passthru[topic] = {}
        daf.message_handler(topic,respond=False)(Passthrough)()
        for command, forward_topic in handler.items():
            passthru[topic][command] = forward_topic
            daf.command_handler(command=command,default=True)(Passthrough.default)
