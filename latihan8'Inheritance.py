"""
Inheritance = pewarisan ( berlaku class ke class )
"""

class Hero:  # TEMPLATE
    # CLASS VARIABEL
    jumlah = 0

    def __init__(self, name, health):
        # INSTANCE VARIABEL
        self.name = name
        self.health = health
        Hero.jumlah += 1

class Hero_intellegent(Hero):
    pass

class Hero_strength(Hero):
    pass


hero1 = Hero('Lina', 100 )    # OBJECT / INSTANCE
hero2 = Hero_intellegent('Aurora', 60)
hero3 = Hero_strength('Axe', 200)

print(hero1.name)
print(hero2.name)
print(hero3.name)