distance = float(input("Enter distance (in km): "))
order_amount = float(input("Enter order amount (₹): "))
user_type = input("Enter user type (Normal/Gold/Platinum): ").lower()
delivery_charge = 50
if order_amount < 1000:
    if distance > 5:
        delivery_charge += (distance - 5) * 10
else:
    delivery_charge = 0
if user_type == "gold":
    discount = 0.20
elif user_type == "platinum":
    discount = 0.30
else:
    discount = 0.0
discount_amount = order_amount * discount
discounted_order = order_amount - discount_amount
final_bill = discounted_order + delivery_charge
print("\nBill Summary")
print(f"User Type: {user_type.capitalize()}")
print(f"Order Amount : ₹{order_amount:.2f}")
print(f"Discount Applied: ₹{discount_amount:.2f}")
print(f"Delivery Charge: ₹{delivery_charge:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")
