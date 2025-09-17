'''Program to accept percentage and entrance marks out of 20 from user, decide student is eligible or not
   1.Per bw 80 to 100 and test marks are more than 15 ->eligible for all streams
   2.Per bw 70 to 80 and test marks more than 10 to 15->eligible for science stream
   Per bw 60 to 70 and test marks more than 5 to 10->eligible for humanities 
   otherwise not eligible'''
per=int(input("Enter Percentage: "))
marks=int(input("Enter Marks"))
if per>80 and per<100:
    if marks>15:
        print("Eligible for all streams")
elif per>70 and per<80:
    if marks>10 and marks<15:
        print("Eligible for science streams")
elif per>60 and per<70:
    if marks>5 and marks<10:
        print("Eligible for humanities")
else:
    print("Not eligible")
