class Interaction:

    def __init__(self, id, addressee="", target=None, opener="", conditional=None, effects=None):
        self.id = id
        self.addressee = addressee
        self.opener = opener

        if target is None:
            self.target = []
        else:
            self.target = target

        if conditional is None:
            self.conditional = []
        else:
            self.conditional = conditional

        if effects is None:
            self.effects = []
        else:
            self.effects = effects

    def perform(self, system, interaction_data):
        '''Method to perform this interaction and trigger the effects'''

        # If the body of the interaction has a conditional, get the effects from evaluating that
        if self.conditional:
            effects = self.conditional.process(system, interaction_data)
        else:
            effects = self.effects

        # Update the system with the last speaker
        system.update_speaker(interaction_data['speaker'])

        # return the list of updated effects
        return effects
