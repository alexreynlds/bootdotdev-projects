import os
from screens.welcome import welcome_screen
from screens.turn import print_turn
from player import Player
from enemy import Goblin


def do_round(player, enemy, turn, prev_turn_log):
    print_turn(turn, player, enemy, prev_turn_log)
    turn_log = list()
    while True:
        choice = int(input(": "))
        if choice < 1 or choice > len(player.actions):
            print("Invalid option")
        else:
            break
    action_name = list(player.actions.keys())[choice - 1]
    action_function = player.actions[action_name]["fn"]

    if player.speed > enemy.speed:
        turn_log.append(action_function(enemy))
        turn_log.append(enemy.do_turn(player))
    else:
        turn_log.append(enemy.do_turn(player))
        turn_log.append(action_function(enemy))

    return turn_log


def main():
    clear = lambda: os.system("clear")
    player = Player(welcome_screen())
    enemy = Goblin()
    round = 0
    playing = True

    # round
    while playing:
        turn = 0
        playing_turn = True
        prev_turn_log = list()

        while playing_turn:
            clear()
            prev_turn_log = do_round(player, enemy, turn, prev_turn_log)
            turn += 1

        round += 1


if __name__ == "__main__":
    main()
