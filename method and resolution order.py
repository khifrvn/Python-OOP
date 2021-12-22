# method resolution order // multiple inheritance

class A:

    def showA(self):
        print("Ini show A")

class B:

    def showB(self):
        print("Ini show B")

class C(A, B):

    def showC(self):
        print("Ini show C")

objek = C()
objek.showA()
objek.showB()
help(objek)  # -------> melihat urutan method