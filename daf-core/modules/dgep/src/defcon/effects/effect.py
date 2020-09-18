class Effect:
    '''Base class to represent an effect;
        is used as the default if no handler is found for an effect, but this
        should be avoided'''

    def __init__(self):
        self.type="DefaultEffect"
        return

    def perform(self, system, interaction_data=None):
        return

    def update(self, system=None, data=None):
        return

    def get_type(self):
        return self.type
