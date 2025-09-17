'''Programs on decision making
1.Write a program to accept choice from user and print result
S print Sunday
M print Monday
Th print thursday
Sa print saturday'''
ch=input("Enter the first letter")
match ch:
    case 'S':
        print("Sunday")
    case 'M':
        print("Monday")
    case 'T':
        print("Tuesday")
    case 'W':
        print("Wednesday")
    case 'Th':
        print("Thursday")
    case 'F':
        print("Friday")
    case 'Sat':
        print("Saturday")
    case _:
        print("invalid input")