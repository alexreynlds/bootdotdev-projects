import os
import sys
import random
from screens.welcome import welcome_screen
from screens.turn import print_turn
from screens.shop import print_shop
from player import Player
from enemy import regular_enemies, boss_enemies


def generate_enemy(round):
    if round == 10 or round == 20:
        # boss round
        enemy_class = random.choice(boss_enemies)
        return enemy_class()
    else:
        enemy_class = random.choice(regular_enemies)
        return enemy_class()


def do_turn(player, enemy, round, turn, prev_turn_log):
    round_over = False
    # Print the turn screen with the previous round log
    print_turn(round, turn, player, enemy, prev_turn_log)
    # print_shop(player)

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

    player.pay_cost(player.actions[action_name])

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
        if round in [0, 5, 10, 15]:
            print_shop(player)

        enemy = generate_enemy(round)

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

        # If the player died - end the game
        if player.health <= 0:
            print("GAME OVER")
            sys.exit()

        # Otherwise, reward them with gold, partially regen their stats and proceed to next round
        print(
            f"Congratulations, you beat {enemy.name}! You earned {enemy.gold_reward} gold!"
        )
        player.gold += enemy.gold_reward

        player.health = min(player.health + 3, player.max_health)
        player.stamina = min(player.stamina + 2, player.max_stamina)
        player.mana = min(player.max_mana + 2, player.max_mana)

        round += 1
        input(f"Press Enter to continue to round {round}...")


if __name__ == "__main__":
    main()
