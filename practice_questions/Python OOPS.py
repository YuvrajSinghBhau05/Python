'''wAP to create a class with name calculator
create four functions of class
Sum
Sub
mult
div'''

class calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        print("Addition is ",a+b)
    def sub(self,a,b):
        print("Subtraction is ",a-b)
    def div(self,a,b):
        print("Division is ",a%b)
    def mult(self,a,b):
        print("Multiplication is ",a*b)
        
obj1=calculator()
obj2=calculator()
obj3=calculator()
obj4=calculator()
obj1.add(4,5)
obj2.sub(8,5)
obj3.div(8,2)
obj4.mult(5,3)
