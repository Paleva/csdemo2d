
class Player():
    """
    Represents a player in a match with their statistics.
    Args:
        username (str): The player's username.
        damage (int): Total damage dealt by the player.
        adr (float): Average Damage per Round (ADR).
        kills (int): Total number of kills by the player.
        assists (int): Total number of assists by the player.
        deaths (int): Total number of deaths by the player.
        kast (int): Percentage of rounds in which the player had a kill, assist, survived, or was traded (KAST).
        impact (float): Impact rating of the player.
        rating (float): Overall rating of the player.
    """
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