class Conditional:
    '''Class to represent a conditional in a Rule or Interaction
       Is also used to nest 'elseif' statements: an elseif is itself a conditional with
       associated resultant effects if it evaluates to True'''

    def __init__(self):

        self.requirements = [] #populated with all requirements that must be fulfilled
        self.effects = [] #the effects to take place if the requirements are fulfilled

        self.elseif_ = None #conditional object corresponding to first elseif after this conditional

        self.else_effects = [] #the effects to take place if none of the requirements and none of the elseif's are fulfilled

        in_else = False

    def process(self, system, interaction_data=None):
        '''Processes this conditional to determine what if any effects should result from it
            Return: the (possibly empty) list of effects'''

        result = True
        effects = []

        # First process the requirements; if any evaluates to false, break out
        for r in self.requirements:
            result = r.test(system, interaction_data)
            if not result:
                break

        # If result is True, use the effects from this conditional; if not, head down the ifelse path if one exists
        if result:
            effects = self.effects
        elif self.elseif_:
            effects = self.elseif_.process(system)

        #if our effects are empty then use else as last resort (if exists; if not, an empty list will be returned)
        if not effects:
            effects = self.else_effects

        return effects
