#Implement list built in functions
my_list=[10, 20, 30, 40, 50]
print("Original list:", my_list)
print("Length of the list: ", len(my_list))
check=int(input("Enter element to check existence: "))
print(f"Is {check} in the list?", check in my_list)
my_list.sort()
print("Sorted list: ", my_list)
my_list.reverse()
print("Reverse list: ", my_list)
copy=my_list[:]
print("Copied list: ", copy)