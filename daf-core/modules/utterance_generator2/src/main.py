import json
import daf
from daf import mongo
import os
from handlers import *

def check_first_run():
    return


if __name__ == '__main__':
    if os.getenv("DEMO","False") == "True":
        check_first_run()
    daf.Module().run(host=('activemq-internal',61613))
