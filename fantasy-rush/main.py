from screens.welcome import welcome_screen
from screens.round import print_round
from player import Player
from enemy import Goblin


def do_round(player, enemy, round):
    print(f"{player.name} is faced against a {enemy.name}")
    print("What do you want to do?\n[1] Attack")
    choice = input(": ")
    print(choice)

    # if choice == "1":
    #     print("attacking")
    #     player.attack(enemy)

    round_log = {"Alex attacked", "goblin Attacked", "goblin died"}

    print_round(round, player, enemy, round_log)


def main():
    player = Player(welcome_screen())
    enemy = Goblin()
    round = 0
    playing = True

    while playing:
        do_round(player, enemy, round)
        round += 1


if __name__ == "__main__":
    main()
