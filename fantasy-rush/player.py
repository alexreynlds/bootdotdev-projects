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
        self.evasion = 0.01

        # modifiers
        self.is_blocking = False

        self.gold = 50

        self.actions = {
            "Attack": {
                "category": "main",
                "fn": self.attack,
                "cost": 0,
                "desc": "A basic attack with your weapon",
            },
            "Heavy Attack": {
                "category": "stamina",
                "fn": self.heavy_attack,
                "cost": 2,
                "desc": "Empower your blow with stamina",
            },
            "Block": {
                "category": "stamina",
                "fn": self.block,
                "cost": 2,
                "desc": "Block your opponents next attack",
            },
            "Dodge": {
                "category": "stamina",
                "fn": self.attack,
                "cost": 1,
                "desc": "Attempt to dodge your opponents next attack",
            },
        }

    def pay_cost(self, action):
        cat = action["category"]
        cost = action.get("cost", 0)

        if cat == "stamina":
            self.stamina -= cost
        elif cat == "mana":
            self.mana -= cost

    def do_turn(self, other):
        action_int = random.randint(1, len(self.actions))
        action_name = list(self.actions.keys())[action_int - 1]
        action_function = self.actions[action_name]["fn"]
        return action_function(other)

    def attack(self, other):
        crit_roll = random.randint(0, 1)
        attack_amount = random.randint(1, self.attack_power)

        if crit_roll <= self.crit_chance:
            attack_amount *= 2
            other.take_damage(attack_amount)
            return f"CRIT! {self.name} attacks {other.name} for {attack_amount} damage"
        else:
            other.take_damage(attack_amount)
            return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def heavy_attack(self, other):
        crit_roll = random.randint(0, 1)
        attack_amount = random.randint(self.attack_power, self.attack_power * 3)

        if crit_roll <= self.crit_chance:
            attack_amount *= 2
            other.take_damage(attack_amount)
            return f"CRIT! {self.name} hits {other.name} with a heavy attack for {attack_amount} damage"
        else:
            other.take_damage(attack_amount)
            return f"{self.name} hits {other.name} with a heavy attack for {attack_amount} damage"

    def block(self, other):
        if self.stamina >= 2:
            self.stamina -= 2
            self.is_blocking = True
            return f"{self.name} prepares to block {other.name}'s attack"

    def heal(self, other):
        heal_amount = random.randint(1, self.max_health // 4)
        new_health = self.health + heal_amount

        if new_health > self.max_health:
            self.health = self.max_health
        else:
            self.health += heal_amount

        # self.health += heal_amount
        return f"{self.name} heals themselves for {heal_amount} HP"

    def take_damage(self, amount):
        self.health -= amount
