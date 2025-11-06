#Append, insert, amd remove elements from a list
my_list=[10, 20, 30, 40, 50]
print("Original list:", my_list)
val=int(input("Enter value to append: "))
my_list.append(val)
print("List after append: ", my_list)
pos=int(input("Enter index to insert value: "))
val=int(input("Enter value to insert: "))
my_list.insert(pos, val)
print("List after insert:", my_list)
value_to_remove=int(input("Enter value to remove: "))
my_list.remove(value_to_remove)
print("List after remove: ", my_list)