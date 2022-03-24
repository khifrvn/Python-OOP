class Hero:  # TEMPLATE
    # CLASS VARIABEL
    jumlah = 0

    def __init__(self, name, health, attack, defence):
        # INSTANCE VARIABEL NIHH
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        Hero.jumlah += 1

    # INI METHOD / VOID FUNCTION (TANPA RETURN)
    def who(self):
        print("My name is :", self.name)

    # INI METHOD DENGAN ARGUMEN
    def healthUp(self, up):
        self.health += up

    # INI METHOD DENGAN RETURN
    def getHelath(self):
        return self.health



hero1 = Hero('Sniper', 100, 500, 50)    # OBJECT / INSTANCE
hero2 = Hero('Sven', 500, 250, 100)
hero3 = Hero('Mirana', 150, 400, 25)

print(hero1.__dict__)
print(hero1.name)
print(Hero.jumlah)
print("="*30)
#==============

hero1.who()
