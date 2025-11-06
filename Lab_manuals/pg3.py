s1=int(input("Enter marks for subject 1"))
s2=int(input("Enter marks for subject 2"))
s3=int(input("Enter marks for subject 3"))
s4=int(input("Enter marks for subject 4"))
s5=int(input("Enter marks for subject 5"))
tot=s1+s2+s3+s4+s5
print("Total marks is: ",tot)
per=tot/500*100
print("Percentage is: ",per)
if per>=95:
    print("GRADE A")
if per>=85 and per<95:
    print("GRADE B")
if per>=70 and per<85:
    print("GRADE C")
if per>=60 and per<70:
    print("GRADE D")
else:
    print("Invalid input")