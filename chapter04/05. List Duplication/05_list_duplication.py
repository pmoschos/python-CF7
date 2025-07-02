# Initialize a list with mixed types, including a nested list
my_list = [1, 2, "Hello", [3, 4, 5]]

# Print each item in the new list and its memory address
# This helps to understand which items are the same objects (sharing the same memory address)
print("At the start:")
for item in my_list:
    print(f"{item} : {id(item)}")

# Create a new list by repeating the original list twice
new_list = my_list * 2
print("\nDuplicated list:", new_list)
print("---------------")

# Modify the first element of the new list
new_list[0] = 100
print("\nModified first element of new_list:", new_list)
print("---------------")

# Modify an element within the nested list inside new_list
# This shows how changes to mutable objects inside lists affect all references
new_list[3][0] = 300
print("\nModified nested list within new_list:", new_list)
print("---------------")

# Print each item in the new list and its memory address
# This helps to understand which items are the same objects (sharing the same memory address)
print("\nAt the end:")
for item in new_list:
    print(f"{item} : {id(item)}")
