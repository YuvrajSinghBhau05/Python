#University admmission
phy=int(input("Enter the physics marks: "))
chem=int(input("Enter the chemistry marks: "))
math=int(input("Enter the maths marks: "))
total=phy+chem+math
avg=total/3
print("Total is- ",total)
print("Average is- ",avg)
if avg>=70 and phy>=60 and chem>=60 and math>=60:
    print("Eligible for admission")
elif math>=90:
    print("Eligible under math special quota")
else:
    print("Not eligible")