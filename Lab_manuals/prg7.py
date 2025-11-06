#Armstrong number
num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if sum==num:
    print(f"{num} is Armstrong")
else:
    print(f"{num}is not Armstrong")
