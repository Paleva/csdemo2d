from awpy import Demo

class Match():
    def __init__(self, parsed_demo: Demo):
        self.map = parsed_demo.header["map_name"]
        self.players = None

    def __repr__(self):
        return f"MAP: {self.map}\nPLAYERS: {self.players}"