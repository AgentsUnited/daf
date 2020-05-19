from .requirement import Requirement

class Event(Requirement):

    def __init__(self, position, moveID):
        children = tree.getChildren()

        self.position = position
        self.moveID = moveID
        self.content = []
        self.requirements = []
        self.speaker = ""

    def test(self, system, interaction_data=None):
        '''Method to test this requirement, inspecting the dialogue history in the system'''
        fulfilled = True

        #Test any requirements that this requirement, er, requires before it's active
        for r in self.requirements:
            if not r.test(system):
                fulfilled = False
                break

        #If the requirements aren't fulfilled, return False now before going any further
        if not fulfilled:
            return False
        else:
            # Set fulfillment to false: i.e. assume the test isn't met
            fulfilled = False

            #Some of the tests need to be inverted - this tells us which ones
            invert = False
            history = system.get_dialogue_history()

            #Select the search range of the dialogue history: last move only, or whole set?
            if self.position == "last":
                start = len(history)-1
                end = len(history)
            elif self.position == "past":
                start = 0
                end = len(history)
            elif self.position == "!last":
                start = len(history)-1
                end = len(history)
                invert = True
            elif self.position == "!last":
                start = 0
                end = len(history)
                invert = True

            #Using the search range, find a move (if exists) that satisfies the requirements
            for i in range(start, end):
                move = history[i]
                fulfilled = (self.moveID == move["moveID"]) and self.test_content(list(move["content"].values())) and self.test_user(move["speaker"])

                #If we've found a move, no need to continue
                if fulfilled:
                    break

        #Do we need to invert the result? Applies if !last or !past are used
        if invert:
            return not fulfilled
        else:
            return fulfilled

    def test_content(self, content):
        '''Method to test the required content against the actual, given, content
            Returns True if there is no required content'''
        if self.content:
            if sorted(self.content) == sorted(move["content"].values()):
                return True
            else:
                return False
        else:
            return True

    def test_user(self, user):
        '''Method to test the required user against the actual, given user
            Returns True if there is no required user'''
        if self.user:
            if self.user == user:
                return True
            else:
                return False
        else:
            return True
