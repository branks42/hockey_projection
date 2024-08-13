from rich.console import Console
from rich.table import Table

from country_codes import COUNTRY_CODES

console = Console()

def print_goalie_stats(p):
    """
    Print the projected stats for a goalie
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Goalie Games Played", style="dim", width=15)
    table.add_column("Goalie Wins")
    table.add_column("Goalie Losses")
    table.add_column("Goalie Ties Overtime")
    table.add_column("Save Percentage")
    table.add_column("Goals Against Average")
    table.add_row(str(p[7]), str(p[8]), str(p[9]), str(p[10]), str(p[11]), str(p[12]))
    console.print(table)

def print_skater_stats(p):
    """
    Print the projected stats for a skater
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Games Played", style="dim", width=15)
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Points")
    table.add_column("Plus Minus")
    table.add_row(str(p[2]), str(p[3]), str(p[4]), str(p[5]), str(p[6]))
    console.print(table)

def show_nationality_options():
    """
    Show the user the nationality options
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Country Code", style="dim", width=12)
    table.add_column("Country")
    for code, country in COUNTRY_CODES.items():
        table.add_row(code, country)
    console.print(table)

def show_position_options():
    """
    Show the user the position options
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Position Options", style="dim", width=12)
    for i in ['C', 'LW', 'RW', 'D', 'G']:
        table.add_row(i)
    console.print(table)