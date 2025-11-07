#Single Inheritance
class A:
    def showA(self):
        print("This is class A")

class B(A):
    def showB(self):
        print("This is class B")

obj=B()
obj.showA()
obj.showB()