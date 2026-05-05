from console import console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich.console import Group
from item import shop_items


def print_shop(player):

    # Player Stats
    # Displaying all of the possible actions the player can take
    actions_table = Table(title="Shop Inventory", show_header=True, border_style="blue")
    categories = {"consumable": [], "equipment": [], "ability": []}

    for i, item in enumerate(shop_items, start=1):
        cat = item.category
        cost = item.cost
        cost_label = f"{cost} {cat}" if cost > 0 else "Free"
        entry = f"[{i}] {item.name} - {cost_label}\n    - {item.desc}"
        categories[cat].append(entry)

    # Get the longest category list to determine the max row (col height)
    max_rows = max(len(v) for v in categories.values())
    for cat in categories:
        categories[cat] += [""] * (max_rows - len(categories[cat]))
        actions_table.add_column(cat.capitalize())

    # Construct the rows of the table and add them
    for row in zip(
        categories["consumable"], categories["equipment"], categories["ability"]
    ):
        actions_table.add_row(*row)

    # Organising the printout and printing it
    body = Group(actions_table)

    header = Text(
        f"Welcome to the shop | {player.gold} Gold",
        style="bold yellow",
        justify="center",
    )

    # Print the shop screen for the user
    console.print(Panel(body, title=header, border_style="green", padding=(1, 2)))

    while True:
        choice = input(">> ")
        if choice == "q":
            break
        if choice.isdigit() and 1 <= int(choice) <= len(shop_items):
            choice = int(choice)
            item = shop_items[choice - 1]
            if player.gold >= item.cost:
                player.gold -= item.cost
                item.effect(player)
                print(f"Bought {item.name}!")
            else:
                print("Not enough gold")
        else:
            print("Invalid option")
