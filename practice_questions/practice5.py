#Program to accept price of 10 different items and provide discount if total exceeds 2000
total=0
for i in range(1,11):
    item=int(input(f"Enter the price of item {i}: "))
    total+=item
if total>2000:
    discount=20/100*total
    finalamt=total-discount
    print("Discount is: ",discount)
    print("final amount is: ",finalamt)
else:
    print("No Discount")
