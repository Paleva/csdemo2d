from awpy import Demo, stats
from player.player import Player

class Parser():
    def __init__(self, parsed_demo: Demo):
        self.parsed_demo = parsed_demo

    def parse_player_stats(self):
        players_adr = stats.adr(self.parsed_demo).tail(10).sort("name") # All round data is in the tail
        players_kast = stats.kast(self.parsed_demo, 5).head(10).sort("name") # All round data is in the head 
        players_rating = stats.rating(self.parsed_demo).head(10).sort("name")
        players_kills = self.parsed_demo.kills.group_by("attacker_name").len().sort("attacker_name")        
        
        players: list[Player] = []
        
        for adr, kst, impact, rating in zip(players_adr.iter_rows(), players_kast.get_column('kast'), players_rating.get_column('impact'), players_rating.get_column('rating'), players_kills.get_column("len")):
            players.append(Player(adr, kst, impact, rating))

        return players
    

        