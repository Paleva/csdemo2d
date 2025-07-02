
class Player():
    def __init__(self, stats):
        self.username = stats[0]
        self.damage = stats[4]
        self.adr = stats[5]

    def __repr__(self):
        return f"USERNAME: {self.username} DMG: {self.damage} ADR: {self.adr}"