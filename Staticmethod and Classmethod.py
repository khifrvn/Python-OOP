class Hero:

    # Private class variabel
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # Tidak berlaku utk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # ========= Static method (decorator) ==========
    # nempel ke object dan class nya

    @staticmethod  #-----> decorator
    def getJumlah2():
        return Hero.__jumlah

    @classmethod  #------> decorator
    def getJumlah3(cls):
        return cls.__jumlah

    # ===============================================
    def getName(self):
        return self.__name

hero1 = Hero('Sniper')
print(Hero.getJumlah1())
print(hero1.getName())

print(Hero.getJumlah3())