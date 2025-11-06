bsal=int(input("Enter the Basic Salary: "))
hra=20/100*bsal
da=10/100*bsal
pf=12/100*bsal
Gsal=bsal+hra+da
netsal=Gsal-pf
print("HRA: ",hra)
print("DA:  ",da)
print("PF:  ",pf)
print("Gross Salary: ",Gsal)
print('Net Salary: ',netsal)
if netsal>=80000:
    print("High Earner")
elif 50000<=netsal<80000:
    print("Mid Earner")
else:
    print("Low Earner")
