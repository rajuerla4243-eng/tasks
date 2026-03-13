class A:
    def displayA(self):
        print("This is class A")

class B(A):
    def displayB(self):
        print("This is class B")

class C:
    def displayC(self):
        print("This is class C")

class D(B, C):
    def displayD(self):
        print("This is class D")

d = D()
d.displayA()
d.displayB()
d.displayC()
d.displayD()