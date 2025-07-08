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
        players_adr = stats.adr(self.parsed_demo).filter(pl.col("side") == "all").sort("name") # All round data is in the tail
        players_kast = stats.kast(self.parsed_demo, 5).filter(pl.col("side") == "all").sort("name") # All round data is in the head 
        players_rating = stats.rating(self.parsed_demo).head(10).sort("name")
        players_kills = self.parsed_demo.kills.group_by("attacker_name").len().sort("attacker_name")        
        players_assists = self.parsed_demo.kills.group_by("assister_name").len().sort("assister_name").remove(pl.col("assister_name").is_null())
        players_deaths = self.parsed_demo.kills.group_by("victim_name").len().sort("victim_name")
        players_usernames = self.parsed_demo.ticks.select("name").unique()

        players: list[Player] = []
        
        for username in players_usernames.get_column("name"):
            dmg_adr = players_adr.row(by_predicate=(pl.col("name") == username)) # 4 index is dmg 5 is adr
            kast = players_kast.row(by_predicate=(pl.col("name") == username)) # 5 index is KAST
            ratings = players_rating.row(by_predicate=(pl.col("name") == username)) # 4 index is impact 5 is rating
            try:
                kills = players_kills.row(by_predicate=(pl.col("attacker_name") == username))
                kill_count = kills[1]
            except pl.exceptions.NoRowsReturnedError:
                kill_count = 0
            try:
                assists = players_assists.row(by_predicate=(pl.col("assister_name") == username))
                assist_count = assists[1]
            except pl.exceptions.NoRowsReturnedError:
                assist_count = 0
            try:
                deaths = players_deaths.row(by_predicate=(pl.col("victim_name") == username))
                death_count = deaths[1]
            except pl.exceptions.NoRowsReturnedError:
                death_count = 0
            dmg = dmg_adr[4] if len(dmg_adr) > 0 else 0
            adr = dmg_adr[5] if len(dmg_adr) > 0 else 0
            kast_value = kast[5] if len(kast) > 0 else 0
            impact = ratings[4] if len(ratings) > 0 else 0
            rating = ratings[5] if len(ratings) > 0 else 0
            players.append(Player(username, dmg, adr, kill_count, assist_count, death_count, kast_value, impact, rating))
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
    

        