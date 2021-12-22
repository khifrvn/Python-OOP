class Hero:  # TEMPLATE

    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence


hero1 = Hero('Sniper', 100, 500, 50)    # OBJECT / INSTANCE
hero2 = Hero('Sven', 500, 250, 100)
hero3 = Hero('Mirana', 150, 400, 25)

print(hero1.__dict__)
print(hero1.name)