#Progarm to accept marks of 5 subjects and print pass or fail
eng=int(input("Enter the English marks: "))
maths=int(input("Enter the Maths marks: "))
science=int(input("Enter the Science marks: "))
phy=int(input("Enter the Physics marks: "))
chem=int(input("Enter the Chemistry marks: "))
total=eng+maths+science+phy+chem
per=total/500*100
print("Total marks obtained: ",total)
print("Percentage is: ",per)
if per>=50:
    print("Pass")
else:
    print("Fail")
