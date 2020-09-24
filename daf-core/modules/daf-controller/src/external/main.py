import os
import json
import daf
from daf import mongo
import activemq as internal
from .handlers import *

# we only want to send data back with responses; don't include the command
daf.set_option("RESPOND_WITH_COMMAND", False)

if __name__ == '__main__':
    internal.host=('activemq-internal',61613)  # for sending to internal
    daf.Module().run(host=('activemq-external',61613))
