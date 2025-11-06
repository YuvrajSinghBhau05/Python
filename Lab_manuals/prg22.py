#Enter values of a tuple at run time
size=int(input("Enter the number of elements in the tuple: "))
values=[]
for i in range(size):
    val=input(F"Enter value {i+1}: ")
    values.append(val)
my_tuple=tuple(values)
print("Tuple:", my_tuple)