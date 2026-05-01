import os
import sys
from screens.welcome import welcome_screen
from screens.turn import print_turn
from player import Player
from enemy import Goblin


def do_turn(player, enemy, round, turn, prev_turn_log):
    round_over = False
    # Print the turn screen with the previous round log
    print_turn(round, turn, player, enemy, prev_turn_log)

    turn_log = list()

    while True:
        # Get the user input for their next action
        while True:
            choice = input(">> ")
            if choice.isdigit() and 1 <= int(choice) <= len(player.actions):
                choice = int(choice)
                break
            print("Invalid option")

        action_name = list(player.actions.keys())[choice - 1]
        action_function = player.actions[action_name]["fn"]
        action_category = player.actions[action_name]["category"]
        action_cost = player.actions[action_name]["cost"]

        if action_category == "stamina" and player.stamina < action_cost:
            print("Not enough stamina")
        elif action_category == "mana" and player.mana < action_cost:
            print("Not enough mana")
        else:
            break

    # If the action is block, do it first
    if action_name == "Block":
        turn_log.append(action_function(enemy))
        turn_log.append(enemy.do_turn(player))
    else:
        # Check which combatent is faster and run the turn
        if player.speed > enemy.speed:
            turn_log.append(action_function(enemy))
            turn_log.append(enemy.do_turn(player))
        else:
            turn_log.append(enemy.do_turn(player))
            turn_log.append(action_function(enemy))

    if player.health <= 0 or enemy.health <= 0:
        round_over = True

    # Return the turn log to be passed into the next turn to get printed
    return (turn_log, round_over)


def main():
    clear = lambda: os.system("clear")
    player = Player(welcome_screen())
    round = 0
    playing = True

    # round
    while playing:
        turn = 0
        enemy = Goblin()

        round_over = False
        playing_turn = True
        prev_turn_log = list()

        while playing_turn:
            clear()
            prev_turn_log, round_over = do_turn(
                player, enemy, round, turn, prev_turn_log
            )

            if round_over:
                break

            turn += 1

        # Player completes round - defeats enemy or dies
        clear()

        if player.health <= 0:
            print("GAME OVER")
            sys.exit()

        print(f"Congratulations, you beat {enemy.name}!")
        input("Press Enter to continue...")

        round += 1


if __name__ == "__main__":
    main()
