from ...defcon.player import Player

class PlayerFactory():

    def __init__(self, tree):
        children = tree.getChildren()
        playerID = children[0].text

        self.player = Player(playerID)

        self.roles = []
        self.max = -1
        self.min = 0

        for i in range(1, len(children)):

            child = children[i]
            label = child.text

            if label == "roles":
                for r in child.getChildren():
                    self.player.roles.append(r.text)
            elif label == "max":
                max = child.getChildren()[0].text

                if max == "undefined":
                    self.player.max = -1
                else:
                    self.player.max = int(max)
            elif label == "min":
                self.player.min = int(child.getChildren()[0].text)

    def get_player(self):
        return self.player
