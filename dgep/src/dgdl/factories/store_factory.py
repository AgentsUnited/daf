from ...defcon.store import Store

class StoreFactory():

    def __init__(self, tree):
        children = tree.getChildren();

        id = children[0].text
        owner = children[1].text
        structure = children[2].text
        visibility = children[3].text

        content = []

        for c in tree.getChildren()[4].getChildren():
            content.append(c.text)

        self.store = Store(id, owner, structure, visibility, content)


    def get_store(self):
        return self.store
