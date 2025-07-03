
class Player():
    def __init__(self, stats, kast, impact, rating):
        self.username = stats[0]
        self.damage = stats[4]
        self.adr = round(stats[5], 1)
        self.kast = round(kast)
        self.impact = round(impact, 2)
        self.rating = round(rating, 2)

    def __repr__(self):
        return f"{self.username} {self.damage} {self.adr} {self.kast} {self.impact} {self.rating}" 