#WAP to print multiples of 3 and 5 with sum and count
a=1
sum=0
count=0
print("Multiples of both 3 and 5 are: ")
while a<=100:
    if a%3==0 and a%5==0:
        print(a)
        count+=1
        sum+=a
    a+=1
print("Sum is:",sum)
print("Count is:",count)
