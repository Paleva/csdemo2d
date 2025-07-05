import sys
import polars as pl

from demoparser2 import DemoParser

from printer.table import TablePrinter
from awpy import Demo

from parser.parser import Parser
from match.match import Match

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
        ["Username", "Kills", "Deaths", "Assists", "Damage", "ADR", "KAST", "Impact", "Rating"],
        [str(player) for player in players]  
    )



    
    teams = parser.parse_teams(players)
    print(teams)
    # table.print_table(
    #     ["Team 1", "Team2"],
    #     [str(team) for team in teams]
    # )
    match = Match(demo, players)

if __name__ == "__main__":
    main()