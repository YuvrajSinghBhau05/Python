#Loan eligibility System
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
existing_loan = float(input("Enter your existing loan amount: "))
cibil_score = int(input("Enter your CIBIL score: "))
eligible = True
if 21 <= age <= 60:
    pass
else:
    print("Rejected: Age must be between 21 and 60.")
    eligible = False
if income >= 25000:
    pass
else:
    print("Rejected: Monthly income must be at least 25,000.")
    eligible = False
if existing_loan <= 0.5 * income:
    pass
else:
    print("Rejected: Existing loan must not exceed 50% of your income.")
    eligible = False
if cibil_score >= 700:
    pass
else:
    print("Rejected: CIBIL score must be at least 700.")
    eligible = False
if eligible:
    print("Eligible for loan.")
else:
    print("Loan application rejected.")
