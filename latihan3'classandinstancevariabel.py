class Hero:  # TEMPLATE
    # CLASS VARIABEL
    jumlah = 0

    def __init__(self, name, health, attack, defence):
        # INSTANCE VARIABEL
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        Hero.jumlah += 1

# MAKE HERO COME TRUE
hero1 = Hero('Sniper', 100, 500, 50)    # OBJECT / INSTANCE
hero2 = Hero('Sven', 500, 250, 100)
hero3 = Hero('Mirana', 150, 400, 25)

print(hero1.__dict__)
print(hero1.name)
print(Hero.jumlah)
