class Rule:
    '''Class representing a rule in a DGDL specification'''

    def __init__(self, id, conditional=None, effects=None):

        self.id = id
        self.conditional = conditional
        self.effects = []#effects

    def process(self, system):
        '''Processes this rule and returns the effects, after testing any conditional
            return: effects '''
        if self.conditional:
            return self.conditional.process(system)
        elif self.effects:
            return self.effects
