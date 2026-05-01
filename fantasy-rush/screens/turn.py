from console import console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich.console import Group


def print_turn(turn, player, enemy, turn_log):

    # Player Stats
    player_table = Table(title=player.name, show_header=False, border_style="blue")
    player_table.add_column("Stat", style="cyan")
    player_table.add_column("Value", style="white")
    player_table.add_row("HP", str(player.health))

    # Enemy Stats
    enemy_table = Table(title=enemy.name, show_header=False, border_style="blue")
    enemy_table.add_column("Stat", style="cyan")
    enemy_table.add_column("Value", style="white")
    enemy_table.add_row("HP", str(enemy.health))

    # Organising the stats into side-by-side columns
    columns = Columns([player_table, enemy_table], expand=True, padding=(0, 10))

    # Creating the turn log from the previous turns data
    log_table = Table(title="Turn Log", show_header=True, border_style="red")
    for log in turn_log:
        log_table.add_row(log)

    # Displaying all of the possible actions the player can take
    actions_table = Table(title="Actions", show_header=True, border_style="blue")
    categories = {"main": [], "stamina": [], "magic": []}

    for i, (name, action) in enumerate(player.actions.items(), start=1):
        cat = action["category"]
        categories[cat].append(f"[{i}] {name}")

    # Get the longest category list to determine the max row (col height)
    max_rows = max(len(v) for v in categories.values())
    for cat in categories:
        categories[cat] += [""] * (max_rows - len(categories[cat]))
        actions_table.add_column(cat.capitalize())

    # Construct the rows of the table and add them
    for row in zip(categories["main"], categories["stamina"], categories["magic"]):
        actions_table.add_row(*row)

    # Organising the printout and printing it
    body = Group(columns, log_table, actions_table)

    header = Text(f"Turn {turn}", style="bold yellow", justify="center")

    console.print(Panel(body, title=header, border_style="green", padding=(1, 2)))
