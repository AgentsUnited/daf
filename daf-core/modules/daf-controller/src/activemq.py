import stomp
import json
import daf

# Module to support sending of activeMQ messages
# Used to forward messages from internal to external or vice versa

host = None

def send_message(topic, message):

    if type(message) is dict:
        message = json.dumps(message)

    daf.log("Sending message {} to {}".format(str(message), topic))

    conn = stomp.Connection12([host], auto_content_length=False)
    conn.connect('admin', 'admin', wait=True)
    conn.send(destination='/topic/' + topic, body=message, headers = {"ttl": 30000})
    conn.disconnect()
