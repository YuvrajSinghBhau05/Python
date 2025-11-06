'''WAP to accept choice from user and print result
1 print hI
2 print  welcome
3 print bye'''
ch=int(input("Enter number from 1-3"))
match ch:
    case 1:
        print("Hi")
    case 2:
        print("Welcome")
    case 3:
        print("Bye")
    case _:
        print("Invalid input")
    
