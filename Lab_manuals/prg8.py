#Base to power using while loop
base=int(input("Enter the base: "))
pow=int(input("Enter the pow: "))
res=1
i=1
while i<=pow:
    res=res*base
    i+=1
print(res)

