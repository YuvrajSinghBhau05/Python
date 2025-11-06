answer="yes"
while answer=="yes":
    takein=input('''Enter your choice:-
                      1 for Addition
                      2 for Subtraction
                      3 for Multiplication
                      4 for remainder
                      or No to stop...''')
    if takein=="no":
        print("stopped calculating")
        break
    take=int(takein)
    a=int(input("Enter the first number:  "))
    b=int(input("Enter the second number;  "))
    add=a+b
    sub=a-b
    mul=a*b
    rem=a%b
    if take==1:
        print("Sum is ",add)
    elif take==2:
        print("Difference is ",sub)
    elif take==3:
        print("Multiplication is ",mul)
    elif take==4:
        print("Remainder is ",rem)
    else:
        print("Invalid input")