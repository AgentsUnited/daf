import re
from .descriptors import *
from content.content_descriptor import _content_descriptors as descriptors

_query_regex = re.compile(r"([^\(\) ]+)\((.+)\)")

def find_content(dialogue_id, speaker, descriptor, move, history):
    content = []
    matches = re.findall(_query_regex, descriptor)

    if matches:
        name = matches[0][0]
        query = matches[0][1]

        if name in descriptors:
            content = descriptors[name](dialogue_id=dialogue_id,speaker=speaker,history=history).find_content(query, move.get("reply",None))

    return content
