#Program to implement inbuilt functions
my_tuple = (10, 20, 30, 20, 40, 50)
print("Tuple:", my_tuple)
                
#len()
print("Length of tuple:", len(my_tuple))

#max()
print("Maximum element:", max(my_tuple))

#min()
print("Minimum element:", min(my_tuple))

#sum()
print("Sum of elements:", sum(my_tuple))

#count()
valcount = 20
print(f"Count of {valcount}:", my_tuple.count(valcount))

#index()
valfind = 30
print(f"Index of {valfind}:", my_tuple.index(valfind))
