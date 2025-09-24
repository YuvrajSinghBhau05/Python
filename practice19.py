speed = int(input("Enter the speed of the vehicle: "))
vehicletype = int(input('''Enter the type of vehicle:-
                          1 for Car
                          2 for Bike
                          3 for Truck: '''))

seatbelt = input("Did the person wear seatbelt? Yes/No: ").lower()
helmet = None  
if vehicletype == 2: 
    helmet = input("Did the person have helmet on their head? Yes/No: ").lower()
eligibility = True
total_fine = 0 
if speed > 80:
    print("Fine Rs2000")
    total_fine += 2000
    eligibility = False
if vehicletype == 1 and seatbelt != 'yes':
    print("Fine Rs1000")
    total_fine += 1000
    eligibility = False
if vehicletype == 2 and helmet != 'yes':
    print("Fine Rs1500")
    total_fine += 1500
    eligibility = False
if vehicletype == 3 and speed > 60:
    print("Fine Rs3000")
    total_fine += 3000
    eligibility = False
if eligibility:
    print("No fine. Drive safe!")
else:
    print(f"You are fined. Total fine amount: Rs{total_fine}")
