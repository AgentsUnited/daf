
class YarnNode:

    def __init__(self, title):
        self.title = title
        self.next = []
        self.opener = ""

    def add_next(self, next_title):
        self.next.append(next_title);

    def set_speaker(self, speaker):
        self.speaker = speaker

    def set_opener(self, opener):
        self.opener = opener
