'''WAP to accept amount and category of toys
and calculate bill, according to below mention toy category with eligible discount
1.Electronic toy, amount more than 1000
discount 5%
2.battery operated toy, amount more than 1500
discount 10%
3.Mechanical toy, amount more than 2000
discount 15%'''
amt=int(input("Enter the amount:"))
ctg=int(input('''Enter the category of toys
                1 for Electronic toy
                2 for Battery operated toy
                3 for Mechanical toy:
                '''))
if ctg==1:
    if amt>1000 and amt<1500:
        discount=5/100*amt
        amt=amt-discount
        print(amt)
    else:
        print(amt)
elif ctg==2:
    if amt>1500 and amt<2000:
        discount=10/100*100
        amt=amt-discount
        print(amt)
    else:
        print(amt)
elif ctg==3:
    if amt>2000:
        discount=15/100*amt
        amt=amt-discount
        print(amt)
    else:
        print(amt)
else:
    print("Please enter the correct category ")
    