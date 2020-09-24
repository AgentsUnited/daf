#!/bin/sh

# script to run the controller
# needs to run as two separate python programs: one to listen for
# external messages; the other to listen for internal messages

python3 -um internal.main &
python3 -um external.main
