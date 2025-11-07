#Constructor Overloading
class Demo:
    def __init__(self, a=None, b=None):
        self.a=a
        self.b=b
    
    def show(self):
        print("a=", self.a, "b=", self.b)
        
d1=Demo()
d1.show()

d2=Demo(28)
d2.show()

d3=Demo(28, 29)
d3.show()