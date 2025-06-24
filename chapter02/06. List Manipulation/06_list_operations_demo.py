# Populate a list with initial values
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add a single element at the end of the list
fruits.append("Berry")
print("After adding Berry:", fruits)

# Add multiple elements at the end of the list
fruits.extend(["Grapes", "Fig"])
print("After adding Grapes and Fig:", fruits)

# Insert an element at a specific position
fruits.insert(1, "Coconut")  # Insert Coconut at position 1
print("After inserting Coconut at position 1:", fruits)

# Update the first element
fruits[0] = "Melon"
print("After updating the first element to Melon:", fruits)

# Update a slice of the list (two elements)
fruits[1:3] = ["A"]  # Replace elements at index 1 and 2
print("After updating two elements:", fruits)

# Delete an element by position using pop()
removed_item = fruits.pop(1)  # Remove the second element
print(f"Removed item: {removed_item}")
print("List after removal:", fruits)

# Delete an element by value using remove()
fruits.remove("Cherry")  # Remove the first occurrence of "Cherry"
print("List after removing Cherry:", fruits)

# Check if a removed item exists in the list
if "Cherry" in fruits:
    print("Cherry still exists in the list")
else:
    print("Cherry doesn't exist in the list")

# Search for an element in the list and get its position
pos = fruits.index("Berry")
print(f"'Berry' is at position {pos} in the list.")