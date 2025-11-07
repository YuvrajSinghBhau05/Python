#Default and Parameterized Constructors
class Demo:
    def __init__(self, x=0):
        self.x=x
        
    def show(self):
        print("VAlue:", self.x)

d1=Demo()
d1.show()

d2=Demo(28)
d2.show()