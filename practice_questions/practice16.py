'''To qualify for a schoalrship student have to go through three screening tests.
1. Aptitude Test(marks out of 100)
2. Coding Test(marks out of 100)
3. Viva (marks out of 50)
to be eligible student have to secure more than 95 in coding test. total of
aptitude and viva should be more than 130, average marks are more than 180'''


apt=int(input("Enter the Aptitude test marks(out of 100):"))
coding=int(input("Enter the Coding test marks(out of 100):"))
viva=int(input("Enter the Viva marks(out of 50)"))
tot=apt+viva
avg=apt+coding+viva/3
if coding>95 and tot>130 and avg>180:
    print("You are eligible for the scholarship")
else:
    print("Sorry, you are not eligible for the scholarship")
