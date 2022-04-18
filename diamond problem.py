# diamond problem
# problem 

class A:

    def show(self):
        print("ini adalah show a")

class B(A):

    def show(self):
        print("ini adalah show b")

class C(A):

    def show(self):
        print("ini adalah show c")

class D(B,C):
    pass

objek = D()
help(objek)
