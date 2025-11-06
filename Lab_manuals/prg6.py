#Factorial of a number
num=int(input("Enter a number to find its factorial: "))
factorial=1
i=1
while i<=num:
    factorial=factorial*i
    i=i+1
print("The factorial of", num, "is:", factorial)
