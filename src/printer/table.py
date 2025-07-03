from rich.table import Table
from rich.console import Console


class TablePrinter():
    def __init__(self, title: str = ""):
        self._table = Table(title=title)
        self._console = Console()

    def print_table(self, columns: list[str], rows: list[str]):
        """
        rows: List of strings that contain the rows information seperated by spaces
        columns: List of column string names
        """ 
        for column in columns:
            self._table.add_column(*column.split(" "))
        
        for row in rows:
            self._table.add_row(*row.split(" "))
            
        self._console.print(self._table)
        