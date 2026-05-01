import random


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

        self.max_health = 10
        self.max_mana = 5
        self.max_stamina = 5

        self.health = 10
        self.mana = 5
        self.stamina = 5

        self.attack_power = 2
        self.armor = 1
        self.crit_chance = 0.10
        self.speed = 5

        # modifiers
        self.is_blocking = False

        self.gold = 0

        self.actions = {
            "Attack": {"category": "main", "fn": self.attack, "cost": 0},
            "Heavy Attack": {"category": "stamina", "fn": self.attack, "cost": 2},
            "Block": {"category": "stamina", "fn": self.block, "cost": 2},
            "Dodge": {"category": "stamina", "fn": self.attack, "cost": 2},
            "Heal": {"category": "mana", "fn": self.attack, "cost": 2},
            "Fire": {"category": "mana", "fn": self.attack, "cost": 2},
        }

    def do_turn(self, other):
        action_int = random.randint(1, len(self.actions))
        action_name = list(self.actions.keys())[action_int - 1]
        action_function = self.actions[action_name]["fn"]
        return action_function(other)

    def attack(self, other):
        crit_roll = random.randint(0, 1)
        attack_amount = random.randint(0, self.attack_power)

        if crit_roll <= self.crit_chance:
            attack_amount *= 2
            other.take_damage(attack_amount)
            return f"CRIT! {self.name} attacks {other.name} for {attack_amount} damage"
        else:
            other.take_damage(attack_amount)
            return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def block(self, other):
        if self.stamina >= 2:
            self.stamina -= 2
            self.is_blocking = True
            return f"{self.name} prepares to block {other.name}'s attack"

    def take_damage(self, amount):
        self.health -= amount
