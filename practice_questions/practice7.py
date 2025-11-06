# program for seat assignment
rno=int(input("Enter the registartion number: "))
if rno>=1 and rno<=61:
    if rno>=1 and rno<=10:
        print("Row 1")
    elif rno>=11 and rno<=20:
        print("Row 2")
    elif rno>=21 and rno<=30:
        print("Row 3")
    elif rno>=31 and rno<=40:
        print("Row 4")
    elif rno>=41 and rno<=50:
        print("Row 5")
    elif rno>=51 and rno<=60:
        print("Row 6")
else:
    print("Please enter valid registration number bewteen 1 to 61")
