# A list containing elements of various data types
items = [1, 2, 3.14, True, "Hello CF6 friends"]

# Iterating through the list and printing each item
for item in items:
    print(item, end=" ")
print()

# A nested list with sublists
nest_list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Printing the entire nested list
print(f"nested list: {nest_list}")  # [[1, 2], [3, 4], [5, 6]]

# Accessing the first sublist in the nested list
print(f"first nested list: {nest_list[0]}")  # [1, 2]

# Accessing an element in the second sublist
print(f"first element of second nested list: {nest_list[1][0]}")  # 3

# Accessing and reversing slices of nested lists
print(f"first nested list: {nest_list[1]}, {nest_list[0]}")  # [3, 4], [1, 2]
print(f"first nested list: {nest_list[:2][::-1]}")  # [[3, 4], [1, 2]]

# Iterating over nested lists and finding the last even number
for outer_item in nest_list:
    for inner_item in outer_item:
        if inner_item % 2 == 0:  # Check if the number is even
            result = inner_item

# Printing the final even number found
print("Final even num:", result)