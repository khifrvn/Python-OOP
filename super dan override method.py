class Hero:  # TEMPLATE
    # CLASS VARIABEL
    jumlah = 0

    def __init__(self, name, health):
        # INSTANCE VARIABEL
        self.name = name
        self.health = health
        Hero.jumlah += 1

    def showInfo(self):
        print("Show info di class Hero")
        print("{} dengan health : {}".format(self.name, self.health))

class Hero_intellegent(Hero):
    def __init__(self, name):
        #Hero.__init__(self, name, 100)
        super().__init__(name, 100)   # ========= SUPER ======
                                      # mengambil method super class
        super().showInfo()

    def showInfo(self):
        print("Show info di subclass hero_intellegent")
        print("{} \n\tTipe: intelegent, \n\thelath :{}".format(self.name,self.health))

class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()


hero1 = Hero('Lina', 100)    # OBJECT / INSTANCE
hero2 = Hero_intellegent('Aurora')
hero3 = Hero_strength('Axe')

print(hero1.name)
