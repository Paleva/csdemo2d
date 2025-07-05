from player.player import Player

class Team():
    """
    Represents a team in a match, containing a list of players.
    Each player is represented by a Player object.
    Args: 
        players (list[Player]): A list of Player objects representing the players in the team.
    """
    def __init__(self, players: list[Player]):
        self.players = players

    def __repr__(self):
        usernames: str = ""
        for username in self.players:
            usernames += f"{username.username} "
        print(usernames)
        return usernames.strip()
    