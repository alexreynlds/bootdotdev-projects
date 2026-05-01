import random


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

        self.max_health = 100
        self.max_mana = 100
        self.max_stamina = 100

        self.health = 100
        self.mana = 100
        self.stamina = 100

        self.attack_power = 2
        self.armor = 1
        self.crit_change = 0.10
        self.speed = 5

        self.gold = 0

        self.actions = {
            "Attack": {"category": "main", "fn": self.attack},
            "Heavy Attack": {"category": "stamina", "fn": self.attack},
            "Block": {"category": "stamina", "fn": self.attack},
            "Dodge": {"category": "stamina", "fn": self.attack},
            "Heal": {"category": "magic", "fn": self.attack},
            "Fire": {"category": "magic", "fn": self.attack},
        }

    def get_name(self):
        return self.name

    def attack(self, other):
        crit_roll = random.randint(0, 1)
        attack_amount = random.randint(0, self.attack_power)

        if crit_roll <= self.crit_change:
            attack_amount *= 2
            other.take_damage(attack_amount)
            return f"CRIT! {self.name} attacks {other.name} for {attack_amount} damage"
        else:
            other.take_damage(attack_amount)
            return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def take_damage(self, amount):
        self.health -= amount
