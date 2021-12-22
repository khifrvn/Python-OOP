class Hero:

    # private class variabel

    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMaximum = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMaximum

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{}  level {}:  \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name, self.__level, self.__health, self.__healthMaximum, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMaximum = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, musuh):
        self.gainExp = 50

hero1 = Hero("Hayabusa", 100, 5, 10)
hero2 = Hero("Alpha", 70, 15, 20)
print(hero1.info)

hero1.gainExp = 150
print(hero1.info)
