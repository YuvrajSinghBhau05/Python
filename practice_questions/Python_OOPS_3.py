'''WAP to create a class with name Student_system
create 5 objects
accept name of student , roll no and their stream
'''
class student_system:
    def accept(self):
        self.name=input("Enter your name")
        self.rollno=int(input("Enter the roll no"))
        stream=input("Enter your stream")
        self.name=name
        self.rollno=rollno
        self.stream=stream
    def display(self):
        print("Name: ",self.name,"Roll no: ",self.rollno,"Stream",self.stream)

obj1=student_system()
obj2=student_system()
obj3=student_system()
obj4=student_system()
obj5=student_system()

obj1.accept()
obj1.display()

obj2.accept()
obj2.display()

obj3.accept()
obj3.display()

obj4.accept()
obj4.display()

obj5.accept()
obj5.display()

