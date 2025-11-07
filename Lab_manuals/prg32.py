#Implement Multiple Classes
class student:
    def __init__(self, name):
        self.name=name
        
class marks:
    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2

s=student("Luna")
m=marks(98,99)

print("Student Name:", s.name)
print("Marks:", m.m1, m.m2)