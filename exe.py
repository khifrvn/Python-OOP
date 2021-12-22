class Hero:

    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attackStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attackStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthStandar

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} : Level {} \n\thealth : {}/{} \n\tattack : {} \n\tarmor : {} ".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print("{} Level up !".format(self.__name))
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attackStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def serang(self, ):
        self.gainExp = 50


hero1 = Hero("Spenser", 100, 20, 30)


hero1.serang()
print(hero1.info)
