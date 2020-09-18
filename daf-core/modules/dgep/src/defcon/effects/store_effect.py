from .effect import Effect

class Store_Effect(Effect):

    def __init__(self, store_action, content, store_name, user):

        self.type = "store"
        self.store_action = store_action
        self.content = content
        self.store_name = store_name
        self.user = user

    def update(self, system=None, update_data=None):

        if not update_data:
            return

        content = update_data['content']

        for k in list(content.keys()):
            if k in list(self.content.keys()):
                self.content[k] = content[k]

    def perform(self, system, interaction_data=None):

        if self.store_name in list(system.commitment_stores.keys()):
            store = system.commitment_stores[self.store_name]

            if store.owner == "shared" or store.owner == self.user:
                if self.store_action == "empty":
                    store.empty()
                elif self.store_action == "add":
                    store.add(self.content)
                elif self.store_action == "remove":
                    store.remove(self.content)
