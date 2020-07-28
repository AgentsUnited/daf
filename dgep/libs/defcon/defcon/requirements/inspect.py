from .requirement import Requirement

class InspectRequirement(Requirement):

    def __init__(self, position, store_name, commitments, user, time):

        self.commitments = commitments

        self.position = position
        self.store_name = store_name
        self.user = user
        self.time = time

    def test(self, system, interaction_data=None):

        if self.store_name in system.commitment_stores.keys():
            store = system.commitment_stores[self.store_name]

            if all(elem in store.content  for elem in self.commitments):
                return True

        return False
