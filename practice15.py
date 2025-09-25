'''WAP to design an app for retail store, calculate final bill and discount on multiple
brands according to the given choice
Woodland-20%
levis-30%
VeroModa-35%
US Polo-40%
User can shop from multiple brands, also with amount exceeding 5000, offer a Gift voucher of Rs500 '''


print('''Welcome to the Retail Store Billing System!)
      Available Brands and Discounts:")
       - Woodland : 20%)
       - Levis : 30%)
       - VeroModa : 35%)
       - US Polo : 40%)
      Type 'done' when you finish shopping.''')
total_original = 0
total_final = 0
while True:
    brand = input("Enter brand name: ").lower()
    if brand == "done":
        break
    if brand == "woodland":
        discount = 0.20
    elif brand == "levis":
        discount = 0.30
    elif brand == "veromoda":
        discount = 0.35
    elif brand == "us polo":
        discount = 0.40
    else:
        print("Invalid brand! Please enter a valid brand.\n")
        continue
    amount_input = input("Enter amount for this brand (integer only): ₹")
    if amount_input.isdigit():
        amount = int(amount_input)
    else:
        print("Invalid amount. Please enter a whole number.\n")
        continue
    discount_amount = amount * discount
    final_amount = amount - discount_amount
    print(f"{brand.title()} - Original: ₹{amount:.2f}, Discount: ₹{discount_amount:.2f}, Final: ₹{final_amount:.2f}\n")
    total_original += amount
    total_final += final_amount
print("\n========== FINAL BILL ==========")
print(f"Total Amount (Before Discount): ₹{total_original:.2f}")
print(f"Total Payable (After Discount): ₹{total_final:.2f}")
if total_final > 5000:
    print("🎁 You received a ₹500 Gift Voucher!")
else:
    print("Spend more than ₹5000 to receive a ₹500 Gift Voucher.")
print("Thank you for shopping with us!")
