from .effect import Effect

class Status_Effect(Effect):

    def __init__(self, status):
        self.type = "status"
        self.status_type = status

    def perform(self, system, interaction_data=None):
        print("Performing status update")

        print(self.status_type)

        if self.status_type == "terminate":
            print("Terminating the system")
            system.terminated = True
