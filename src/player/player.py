
class Player():
    def __init__(self, username, damage, adr, kills, assists, deaths, kast, impact, rating):
        self.username = username
        self.damage = damage
        self.adr = round(adr, 1)
        self.kast = round(kast)
        self.impact = round(impact, 2)
        self.rating = round(rating, 2)
        self.kills = kills
        self.assists = assists
        self.deaths = deaths

    def __repr__(self):
        return f"{self.username} {self.kills} {self.deaths} {self.assists} {self.damage} {self.adr} {self.kast} {self.impact} {self.rating}" 