import daf
from handlers import *


if __name__ == '__main__':
    daf.log("WOOL module is starting")
    daf.Module().run(host=('activemq-internal',61613))
