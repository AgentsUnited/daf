import json
from daf import mongo
import daf
import activemq as external
from .handlers import *

def init():
    # the internal listener is a little different; we can't decorate the handler class
    # because we only know the available platforms at runtime. So we do it manually,
    # directly accessing the daf decorator functions

    col = mongo.get_column("dialogue_topics")
    result = col.find({})

    if result:
        for r in result:
            if "platform" in r:
                destination = r["platform"] + "/response"
                daf.message_handler(destination, respond=False)(ResponseHandler)()
                destination = r["platform"] + "/dialogue_moves"
                daf.message_handler(destination, respond=False)(ResponseHandler)()

if __name__ == '__main__':
    external.host=('activemq-external',61613)  # for sending to external
    init()
    daf.Module().run(host=('activemq-internal',61613))
