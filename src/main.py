import sys
from awpy import Demo, stats
from match.round import Round
from player.player import Player

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <argument>")
        sys.exit(1)

    argument = sys.argv[1]
    
    demo = Demo(argument, verbose=True)
    demo.parse()

    adr_all = stats.adr(demo.damages)
    players = []
    for player in adr_all.tail(10).iter_rows():
        players.append(Player(player))
    print(players)

    rounds = []
    for round in demo.rounds.iter_rows():
        rounds.append(Round(round))

    # print(rounds)



if __name__ == "__main__":
    main()