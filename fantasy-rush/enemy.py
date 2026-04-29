import random


class Enemy:
    def __init__(self, name, attack, health, armor):
        self.name = name
        self.attack_power = attack
        self.health = health
        self.armor = armor

    def attack(self, other):
        attack_amount = random.randint(0, self.attack_power)
        print(f"{self.name} attacks {other.name} for {attack_amount} damage")
        other.take_damage(self.attack_power)

    def take_damage(self, amount):
        self.health -= amount


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 1, 10, 0)
