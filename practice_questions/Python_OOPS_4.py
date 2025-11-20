'''Create  a class check()
create a functio with name accept() that accepts a number
then create function verify() to check if a number is even for positive numbers
and create a function validate() to check if a number is positive or negative'''


class check:
    def accept(self):
        self.num=int(input("Enter a Number"))

    def verify(self):
        if self.num%2==0:
            print("Number is even")
            
        else:
            print("Number is odd")

    def validate(self):
        if self.num>0:
            print("Number is positive")
            self.verify()
        else:
            print("Number is negative")

    
    
obj1=check()
obj1.accept()
obj1.validate()
