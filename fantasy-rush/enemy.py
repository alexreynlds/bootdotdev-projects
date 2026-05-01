import random


class Enemy:
    def __init__(self, name, attack, health, mana, stamina, armor, speed):
        self.name = name

        self.max_health = health
        self.max_mana = mana
        self.max_stamina = stamina

        self.health = health
        self.mana = mana
        self.stamina = stamina

        self.attack_power = attack
        self.armor = armor
        self.speed = speed

        # modifiers
        self.is_blocking = False

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
        super().__init__("Goblin", 1, 10, 0, 5, 0, 2)
        self.speed = 2
