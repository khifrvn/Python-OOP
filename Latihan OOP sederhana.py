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

    def serang(self, lawan):
        print(self.name + ' Menyerang ' + lawan.name)
        serangan = int(input("Serang dengan : "))
        lawan.diserang()
        if serangan < int(self.attack):
            print(lawan.name, 'Terkena damage sebesar: ', serangan)
            print("Sisa defence : ", lawan.defence - serangan)
        elif serangan > int(self.attack):
            print("Tidak bisa attack karena melebihi kekuatan")
        elif serangan == lawan.defence:
            print(lawan.name, "Defeated")
        else:
            print("Attack gagal")



    def diserang(self):
        print(self.name + ' Diserang ')




hero1 = Hero('Sniper', 100, 500, 50)    # OBJECT / INSTANCE
hero2 = Hero('Sven', 500, 250, 100)
hero3 = Hero('Mirana', 150, 400, 25)

hero1.serang(hero2)
