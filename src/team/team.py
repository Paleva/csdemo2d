from player.player import Player

class Team():
    def __init__(self, side = "all", players: list[Player] = None):
        self.side = side
        self.players = players

    def __repr__(self):
        pass
