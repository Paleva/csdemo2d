import polars as pl

from awpy import Demo, stats
from player.player import Player

class Parser():
    def __init__(self, parsed_demo: Demo):
        self.parsed_demo = parsed_demo

    def parse_player_stats(self) -> list[Player]:
        """
        Returns a list with Player objects for each player containing the basic stats for them
        """
        players_adr = stats.adr(self.parsed_demo).tail(10).sort("name") # All round data is in the tail
        players_kast = stats.kast(self.parsed_demo, 5).head(10).sort("name") # All round data is in the head 
        players_rating = stats.rating(self.parsed_demo).head(10).sort("name")
        players_kills = self.parsed_demo.kills.group_by("attacker_name").len().sort("attacker_name")        
        players_assists = self.parsed_demo.kills.group_by("assister_name").len().sort("assister_name").remove(pl.col("assister_name").is_null())
        players_deaths = self.parsed_demo.kills.group_by("victim_name").len().sort("victim_name")

        players: list[Player] = []
        
        for username, damage, adr, kills, assists, deaths, kst, impact, rating in zip(
            players_adr.get_column("name"),
            players_adr.get_column("dmg"),
            players_adr.get_column("adr"), 
            players_kills.get_column("len"),
            players_assists.get_column("len"),
            players_deaths.get_column("len"),
            players_kast.get_column('kast'), 
            players_rating.get_column('impact'), 
            players_rating.get_column('rating') 
            ):
            players.append(Player(username, damage, adr, kills, assists, deaths, kst, impact, rating))

        return players
    

        