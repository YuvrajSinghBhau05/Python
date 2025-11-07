#Abstract Class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def area(self):
        print("Area:", 10*20)

obj=Rectangle()
obj.area()