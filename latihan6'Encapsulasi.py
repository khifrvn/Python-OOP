"""
encapsulasi :
    - buat semua variabel private
    - getter  and   setter
         \--------------\
    mengambil var   mensetting var
"""

class Hero:  # TEMPLATE
    # ==== CLASS VARIABEL ====
    jumlah = 0

    def __init__(self, name, health, attack, defence):
        # ==== INSTANCE VARIABEL ====
        self.__name = name
        self.__health = health
        self.attack = attack
        self.defence = defence
        Hero.jumlah += 1

        # ==== INSTANCE VARIABEL (PRIVATE) ====
        self.__private = "Private"  # ===> Assignment diluar class

        # ==== INSTANCE VARIABEL (PROTECTED) ====
        self._protected = "Protected"

    # INI METHOD / VOID FUNCTION (TANPA RETURN)
    def who(self):
        print("My name is :", self.__name)

    # INI METHOD DENGAN ARGUMEN
    def healthUp(self, up):
        self.__health += up

    # INI METHOD DENGAN RETURN
    def getHealth(self):
        return self.__health

    # =================================================

    # GETTER
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # SETTER

    def diserang(self, attack):
        self.__health -= attack


# AWAL DARI GAME

hero1 = Hero('Sniper', 100, 500, 50)    # OBJECT / INSTANCE
hero2 = Hero('Sven', 500, 250, 100)
hero3 = Hero('Mirana', 150, 400, 25)

# GAME BERJALAN

print(hero1.getName())
print(hero1.getHealth())
hero1.diserang(50)
print(hero1.getHealth())

