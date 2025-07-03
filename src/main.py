import sys
import polars as pl

from printer.table import TablePrinter
from awpy import Demo

from parser.parser import Parser
from match.round import Round
from player.player import Player

def main():

    pl.Config.set_tbl_rows(40)
    pl.Config.set_tbl_cols(100)

    if len(sys.argv) < 2:
        print("Usage: python main.py <argument>")
        sys.exit(1)

    argument = sys.argv[1]
    
    demo = Demo(argument, verbose=True)
    demo.parse()

    parser = Parser(demo)
    players = parser.parse_player_stats()
    table = TablePrinter("Game stats")
    table.print_table(
        ["Username", "Damage", "ADR", "KAST", "Impact", "Rating"],
        [str(player) for player in players]  
    )
 

  

    rounds = []
    for round in demo.rounds.iter_rows():
        rounds.append(Round(round))

    




if __name__ == "__main__":
    main()