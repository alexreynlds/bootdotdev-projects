import random


class Enemy:
    def __init__(self, name, gold, attack, health, mana, stamina, speed):
        self.name = name
        self.gold_reward = gold

        self.max_health = health
        self.max_mana = mana
        self.max_stamina = stamina

        self.health = health
        self.mana = mana
        self.stamina = stamina

        self.attack_power = attack
        self.speed = speed

        # modifiers
        self.is_blocking = False

        self.actions = {
            "Attack": {"category": "main", "fn": self.attack, "cost": 0},
        }

    def pay_cost(self, action):
        cat = action["category"]
        cost = action.get("cost", 0)

        if cat == "stamina":
            self.stamina -= cost
        elif cat == "mana":
            self.mana -= cost

    def do_turn(self, other):
        # Keep rolling a move until the enemy has enough resources to use it
        while True:
            action_int = random.randint(1, len(self.actions))
            action_name = list(self.actions.keys())[action_int - 1]
            action_cat = self.actions[action_name]["category"]
            action_cost = self.actions[action_name]["cost"]

            if action_cat == "mana" and self.mana < action_cost:
                continue

            elif action_cat == "stamina" and self.stamina < action_cost:
                continue

            break

        action_function = self.actions[action_name]["fn"]
        action = self.actions[action_name]

        if other.is_blocking:
            other.is_blocking = False
            return f"{self.name} tried to {action_name}, but failed as {other.name} was blocking!"

        evasion_check = random.random()
        if evasion_check <= other.evasion:
            return f"{self.name} tried to {action_name}, but {other.name} evaded the attack"

        self.pay_cost(action)
        return action_function(other)

    def attack(self, other):
        attack_amount = random.randint(0, self.attack_power)
        other.take_damage(attack_amount)
        return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def take_damage(self, amount):
        self.health -= amount


# Regular enemies
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 2, 1, 10, 0, 5, 2)
        self.actions["Throw Rock"] = {
            "category": "stamina",
            "fn": self.throw_rock,
            "cost": 1,
        }

    def throw_rock(self, other):
        attack_amount = random.randint(1, self.attack_power * 2)
        other.take_damage(attack_amount)
        return f"{self.name} threw a rock at {other.name}... dealing {attack_amount} damage..."


class Bear(Enemy):
    def __init__(self):
        super().__init__("Bear", 3, 2, 20, 0, 10, 5)
        self.actions["Scratch"] = {
            "category": "stamina",
            "fn": self.scratch,
            "cost": 2,
        }

    def scratch(self, other):
        attack_amount = random.randint(1, self.attack_power)
        other.take_damage(attack_amount)
        return f"{self.name} viciously scratches {other.name} dealing {attack_amount} damage"


# Bosses
class Hydra(Enemy):
    def __init__(self):
        super().__init__("Hydra", 2, 1, 50, 20, 0, 2)
        self.speed = 2

        self.actions = {
            "Savage Bite": {"category": "main", "fn": self.savage_bite, "cost": 0},
            "Regrow Head": {"category": "mana", "fn": self.regrow_head, "cost": 5},
        }

    def savage_bite(self, other):
        attack_amount = random.randint(1, self.attack_power)
        other.take_damage(attack_amount)
        return f"{self.name} attacks {other.name} for {attack_amount} damage"

    def regrow_head(self, other):
        heal_amount = random.randint(5, 15)
        self.health += heal_amount
        if self.health > 50:
            self.health = 50
        return f"{self.name} regrows one of its heads, healing themselves for {heal_amount}"


regular_enemies = [Goblin, Bear]
boss_enemies = [Hydra]
