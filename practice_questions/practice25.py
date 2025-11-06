#Online examination result
correctans=int(input("Enter the number of correct answers:"))
wrongans=int(input("Enter the number of wrong answers:"))
unattempted=int(input("Enter the number of unattempted questions:"))
correct=4
wrong=-1
unatt=0
s1=correctans*correct
s2=wrong*wrongans
score=s1-s2
if score>=180:
    print("Excellent")
elif 120<=score<=179:
    print("Good")
elif 60<=score<=119:
    print("Average")
elif score<60:
    print("fail")
else:
    print("Invalid input")
if wrongans>correctans:
    print("improve accuracy")
else:
    print("keep it up")
