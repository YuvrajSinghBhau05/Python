#Movie ticket pricing
age=int(input("Enter your age: "))
movietype=input("Enter movie type: 2D/3D ").lower()
day=input("Weekday/Weekend: ").lower()
baseprice=200
if movietype=='3d':
    baseprice+=100
if day=='weekend':
    baseprice+=50
if age<12:
    discount=50/100*baseprice
    finalprice=baseprice-discount
    print("Final price:",finalprice)
elif age>60:
    discount=30/100*baseprice
    finalprice=baseprice-discount
    print("Final price:",finalprice)
    
