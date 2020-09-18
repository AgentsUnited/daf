class Store:

    def __init__(self, id, owner, structure, visibility, content):
        self.id = id
        self.owner = owner
        self.structure = structure
        self.visibility = visibility
        self.content = content

    def add(self, content):

        if self.structure == "stack" or self.structure == "queue":
            for c in content:
                self.content.insert(0, c)
        else:
            self.content.extend(content)
            self.content = list(set(self.content))

    def remove(self, content):
        if self.structure == "stack":
            self.content.pop(0)
        elif self.structure == "queue":
            self.content.pop()
        else:
            self.content = list(set(self.content) - set(content))

    def empty(self):
        self.content = []

    def __str__(self):
        string = "StoreID: " + self.id
        string += "\nOwner: " + self.owner
        string += "\nStructure: " + self.structure
        string += "\nVisibility: " + self.visibility
        string += "\nContent: " + str(self.content)

        return string
