class DialogueManager:
    '''The DialogueManager class store and keeps track of dialogue frameworks
        Can be overriden by specific applications that need a bespoke method of handling these things'''

    def __init__(self):
        self.frameworks = {}

    def new_dialogue(self, name, parent=None):
        if name in list(self.frameworks.keys()):
            system = copy.deepcopy(self.frameworks[name])
            if parent is not None:
                system.parent = parent
            return system

    def register_dialogue_framework(self, name, system):
        self.frameworks[name] = system
