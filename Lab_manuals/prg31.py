#Class student- Methods and Objects
class student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
        
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)

s=student("Rohan", 28)
s.display()