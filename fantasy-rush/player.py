import random


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.health = 100
        self.mana = 100
        self.stamina = 100
        self.gold = 0
        self.attack_power = 2
        self.armor = 1

    def get_name(self):
        return self.name

    def attack(self, other):
        print("aa")
        attack_amount = random.randint(0, self.attack_power)
        print(f"{self.name} attacks {other.name} for {attack_amount} damage")
        other.take_damage(attack_amount)

    def take_damage(self, amount):
        self.health -= amount
