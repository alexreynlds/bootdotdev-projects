import random


class Enemy:
    def __init__(self, name, attack, health, armor):
        self.name = name
        self.attack_power = attack
        self.health = health
        self.armor = armor
        self.actions = {
            "Attack": {"category": "main", "fn": self.attack},
        }

    def do_turn(self, other):
        action_int = random.randint(1, len(self.actions))
        action_name = list(self.actions.keys())[action_int - 1]
        action_function = self.actions[action_name]["fn"]
        return action_function(other)

    def attack(self, other):
        attack_amount = random.randint(0, self.attack_power)
        other.take_damage(attack_amount)
        return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def take_damage(self, amount):
        self.health -= amount


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 1, 10, 0)
        self.speed = 2
