import polars as pl

from awpy import Demo, stats
from player.player import Player
from match.team import Team

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
    
    def parse_teams(self, players: list[Player]) -> list[Team]:
        teams: list[Team] = []
        teams = self.parsed_demo.ticks.filter(pl.col("round_num") <= 12).group_by(["side", "name"]).all().select(["name", "side"])
        team_t = teams.filter(pl.col("side") == "t").select("name").to_series()
        team_ct = teams.filter(pl.col("side") == "ct").select("name").to_series()

        team1 = [player for player in players if player.username in team_t]
        team2 = [player for player in players if player.username in team_ct]

        if len(team1) + len(team2) != len(players):
            raise ValueError("Not all players could be assigned to teams")

        return [Team(team1), Team(team2)]
    

        