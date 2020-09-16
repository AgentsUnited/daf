import daf
import activemq as external
from .handlers import *

def init():
    # the internal listener is a little different; we can't decorate the handler class
    # because it relies on a dynamic config file; so it needs to be done manually
    # using the decorator functions directly

    with open("internal/modules.txt", "r") as modules:
        for module in modules.readlines():
            module = module.strip()

            if module == "" or module[0] == "#": # ignore blank lines and comments
                continue

            destination = module + "/response"
            daf.message_handler(destination, respond=False)(ResponseHandler)()

if __name__ == '__main__':
    external.host=('activemq-external',61613)  # for sending to external
    init()
    daf.Module().run(host=('activemq-internal',61613))
