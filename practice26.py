#ATM Transaction
accbalance=int(input("Enter your account balance; "))
amtwithdraw=int(input("Enter the withdraw amount: "))
acctype=input("Enter your account type Savings/Current?: ").lower()
day=input("Enter the withdrawal day: weekday/weekend?; ").lower()
extra=0
limit=0
if day=='weekend':
    extra=50
elif day=='weekday':
    extra=0
else:
    print("Invalid day")
    exit()
total=amtwithdraw+extra
if acctype=='savings':
    limit=25000
elif acctype=='current':
    limit=50000
else:
    print("Valid account type: ")
    exit()
if amtwithdraw>limit:
    print("Failure!!! Amount exceeds limit")
elif accbalance<total+1000:
    print("Failure!! Insufficient balance")
else:
    print("Withdrawal successful")
    print("Updated balance:",accbalance-total)


