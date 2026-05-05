class Item:
    def __init__(self, name, cost, category, effect, desc):
        self.name = name
        self.cost = cost
        self.category = category
        self.effect = effect
        self.desc = desc


def apply_health_potion(player):
    player.health = min(player.health + 5, player.max_health)


def apply_mana_potion(player):
    player.mana = min(player.mana + 5, player.max_mana)


def apply_stamina_potion(player):
    player.stamina = min(player.stamina + 5, player.max_stamina)


def apply_lightning_boots(player):
    player.speed += 1


def apply_lucky_clover(player):
    player.crit_change += 0.05


def apply_heal_spell_tome(player):
    player.actions["Heal"] = {
        "category": "mana",
        "fn": player.heal,
        "cost": 0,
        "desc": "Heal yourself",
    }


def apply_fire_spell_tome(player):
    player.actions["Fire"] = {
        "category": "mana",
        "fn": player.attack,
        "cost": 2,
        "desc": "Set your opponent on fire",
    }


health_potion = Item("Health Potion", 3, "consumable", apply_health_potion, "Health")
mana_potion = Item("Mana Potion", 3, "consumable", apply_mana_potion, "mana")
stamina_potion = Item("Stamina Potion", 3, "consumable", apply_stamina_potion, "Stam")

lightning_boots = Item("Lightning Boots", 5, "equipment", apply_lightning_boots, "b")
lucky_clover = Item("Lucky Clover", 5, "equipment", apply_lucky_clover, "b")

heal = Item("Heal Spell Tome", 3, "ability", apply_heal_spell_tome, "heal")
fire = Item("Fire Spell Tome", 3, "ability", apply_fire_spell_tome, "fire")

shop_items = [
    health_potion,
    mana_potion,
    stamina_potion,
    lightning_boots,
    lucky_clover,
    heal,
    fire,
]
