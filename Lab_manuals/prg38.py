#Method Overloading
class Demo:
    def add(self, a=0, b=0, c=0):
        print("Sum:", a+b+c)
        
obj=Demo()
obj.add()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)