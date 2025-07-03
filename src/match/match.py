from awpy import Demo
from match.round import Round

class Match():
    def __init__(self, parsed_demo):
        self.map = parsed_demo.header["map_name"]
        self.rounds = self._parse_round(parsed_demo)
        self.players = None

    def _parse_round(self, parsed_demo):
        rounds = []
        for round in parsed_demo.rounds.iter_rows():
            rounds.append(Round(round))
        return rounds

    def __repr__(self):
        return f"MAP: {self.map}\nPLAYERS: {self.players}"