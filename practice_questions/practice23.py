#program to input multiples of 3 using for loop
s=int(input("Enter the starting range: "))
e=int(input("Enter the end range: "))
sum=0
count=0
for i in range(s,e+1):
    if i%3==0:
        print(i,end=" ")
        count+=1
        sum+=i
print("\nSum is: ",sum)
print("Count is: ",count)
