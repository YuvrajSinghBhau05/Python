'''Generate monthly bill electricity
for first 100 ut->rs 2 per ut
for 100 to 200 ut->rs 3 per ut
for 200->300 ut->rs 4 per ut
more than 300 ut-> rs 5 per ut
bill more than 1000 give 5% discount'''
units=int(input("Enter the number of units consumed: "))
if units<= 100:
    bill=units*2
elif units<=200:
    bill=(100*2)+(units-100)*3
elif units<=300:
    bill=(100*2)+(100*3)+(units-200)*4
else:
    bill=(100*2)+(100*3)+(100*4)+(units-300)*5
if bill>1000:
    discount=bill*0.05
    bill-=discount
    print(f"Discount of ₹{discount:.2f} applied.")
print(f"Total electricity bill: ₹{round(bill, 2)}")
