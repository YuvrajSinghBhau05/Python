#E-commerce discount calculator
pp=int(input("Enter the product price: "))
ut=int(input('''Enter the user type: 
             1 for REGULAR
             2 for PREMIUM
             3 for VIP.
             '''))
discount=0
if ut==1:
    if pp<500:
        discount=5/100*pp
        fp=pp-discount
        print("You got a discounted price for being our REGULAR member:",fp)
    elif pp>=500:
        discount=10/100*pp
        fp=pp-discount
        print("You got a discounted price for being our REGULAR member: ",fp)
if ut==2:
    if pp<1000:
        discount=15/100*pp
        fp=pp-discount
        print("You got a discounted price for being our PREMIUM member:",fp)
    elif pp>=1000:
        discount=20/100*pp
        fp=pp-discount
        print("You got a discounted price for being our PREMIUM member: ",fp)
if ut==3:
        discount=25/100*pp
        fp=pp-discount
        print("You got a discounted price for being our VIP member:",fp)
fp = pp - discount
ch = input("How do you want to pay: Online/Offline: ").lower()
if ch == 'online':
    ed = 5 / 100 * fp
    fp = fp - ed
    print("Additional 5% discount applied for online payment. Final price:", fp)
else:
    print("No additional discount. Final price:", fp)



'''pp = int(input("Enter the product price: "))
discount = 0
if ut == 1:
    if pp < 500:
        discount = 5 / 100 * pp
    else:
        discount = 10 / 100 * pp
    print("You got a discounted price for being our REGULAR member:", pp - discount)
elif ut == 2:
    if pp < 1000:
        discount = 15 / 100 * pp
    else:
        discount = 20 / 100 * pp
    print("You got a discounted price for being our PREMIUM member:", pp - discount)
elif ut == 3:
    discount = 25 / 100 * pp
    print("You got a discounted price for being our VIP member:", pp - discount)
else:
    print("Invalid user type")
    exit()
fp = pp - discount
ch = input("How do you want to pay: Online/Offline: ").lower()
if ch == 'online':
    ed = 5 / 100 * fp
    fp = fp - ed
    print("Additional 5% discount applied for online payment. Final price:", fp)
else:
    print("No additional discount. Final price:", fp)'''
                                                                                
