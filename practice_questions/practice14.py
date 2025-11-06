'''WAP to design an app for movie ticket booking 
a-first accept choice of seat(classic @100/ premium @300 / Recliner @500)
b- accept number of seats 
c- now according ot amount provide offers
1. amount bewteen 500 to 1500
offers include(choice of a meal worth RS 200 or 2% discount)
2. amount worth more than 1500
offers include (choice of a meal worth RS 500 or 4% discount)'''
seats=int(input('''Enter the choice of seats
                   1 for Classic @100
                   2 for Premium @300
                   3 for Recliner @500: '''))
nseats=int(input("Enter the number of seats: "))
if seats==1:
    amt=100*nseats
elif seats==2:
    amt=300*nseats
elif seats==3:
    amt=500*nseats
if amt>=500 and amt<=1500:
    ch=input("Do want a meal worth Rs200 or discount of 2%:")
    if ch=='meal':
        print("You got a free meal of worth RS200")
    else:
        discount=2/100*amt
        amt-=discount
        print("Your discounted total is", amt)
elif amt>1500:
    ch=input("Do want a meal worth Rs400 or discount of 4%:")
    if ch=='meal':
        print("You got a free meal of worth RS400")
    else:
        discount=4/100*amt
        amt-=discount
        print("Your discounted total is", amt)
