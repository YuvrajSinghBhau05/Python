#Multlevel Inheritance
class A:
    def showA(self):
        print("This is class A")

class B(A):
    def showB(self):
        print("This is class B")
        
class C(B):
    def showC(self):
        print("This is class C")

obj=C()
obj.showA()
obj.showB()
obj.showC()