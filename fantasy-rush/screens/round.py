from console import console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich.console import Group


def print_round(round, player, enemy, round_log):

    player_table = Table(title=player.name, show_header=False, border_style="blue")
    player_table.add_column("Stat", style="cyan")
    player_table.add_column("Value", style="white")
    player_table.add_row("HP", str(player.health))

    enemy_table = Table(title=enemy.name, show_header=False, border_style="blue")
    enemy_table.add_column("Stat", style="cyan")
    enemy_table.add_column("Value", style="white")
    enemy_table.add_row("HP", str(enemy.health))

    columns = Columns([player_table, enemy_table], expand=True, padding=(0, 10))

    log_table = Table(title="Round Log", show_header=True, border_style="red")
    for log in round_log:
        log_table.add_row(log)

    body = Group(columns, log_table)

    header = Text(f"Round {round}", style="bold yellow", justify="center")

    console.print(Panel(body, title=header, border_style="green", padding=(1, 2)))
