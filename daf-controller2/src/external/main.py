import daf
import activemq as internal
from .handlers import *

daf.set_option("RESPOND_WITH_COMMAND", False)

if __name__ == '__main__':
    internal.host=('activemq-internal',61613)  # for sending to internal
    daf.Module().run(host=('activemq-external',61613))
