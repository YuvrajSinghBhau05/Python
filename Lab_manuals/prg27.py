#Program to remove items from set using discard, pop and remove method
my_set = {10, 20, 30, 40, 50}
print("Original set:", my_set)

my_set.remove(20)
print("After remove:", my_set)

my_set.discard(30)
print("After discard:", my_set)

removed_item = my_set.pop()
print("After pop():", my_set)
print("Popped element:", removed_item)
