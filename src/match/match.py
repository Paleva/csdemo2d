from awpy import Demo
from match.round import Round
from player.player import Player

class Match():
    def __init__(self, parsed_demo: Demo, players: list[Player]):
        self.map = parsed_demo.header["map_name"]
        self.rounds = self._parse_rounds(parsed_demo)
        self.players = players

    def _parse_rounds(self, parsed_demo):
        rounds = []
        for round in parsed_demo.rounds.iter_rows():
            rounds.append(Round(round))
        return rounds

    def __repr__(self):
        return f"MAP: {self.map}\nPLAYERS: {self.players}"