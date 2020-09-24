import json
import daf
from daf import mongo
import os
from handlers import *

if __name__ == '__main__':
    daf.Module().run(name="UtteranceGenerator", host=('activemq-internal',61613))
