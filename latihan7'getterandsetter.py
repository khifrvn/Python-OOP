class Hero:  # TEMPLATE
    # ==== CLASS VARIABEL ====
    __jumlah = 0

    def __init__(self, name, health, attack):
        # ==== INSTANCE VARIABEL ====
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__info = "Name : {} \nhealth : {}".format(self.__name,self.__health)
        Hero.__jumlah += 1

    @property   # ----- > menganggap method menjadi variabel
    def info(self):
        return self.__info

    @property
    def health(self):
        pass

    @health.getter
    def health(self):
        return self.__health

    @health.setter
    def health(self, input):
        self.__health = input

    @health.deleter
    def health(self):
        print("Delete health")
        self.__health = None

hero1 = Hero('Sniper', 100, 500)    # OBJECT / INSTANCE
hero2 = Hero('Sven', 500, 250)
hero3 = Hero('Mirana', 150, 400)

 #==============================================


print(hero1.info)
print("Merubah health")
print("Getter and setter untuk _health")
print(hero1.health)

hero1.health = 1000
print("Setelah dirubah :", hero1.health)
print("mendelete health")

del hero1.health
print("Setelah didelete :", hero1.health)