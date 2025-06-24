# Define a tuple of students
students = "Alice", "Bob", "Charlie"

# Check the type of the tuple
print(type(students))

# Iterate over the tuple with index and value
for index, student in enumerate(students):
    print(f"{index} : {student}")

# Enhanced for-loop to iterate over values only
for student in students:
    print(student)

# Unpacking tuple elements into variables
first_st, second_st, third_st = students

print(f"first_st: {first_st}")
print(f"second_st: {second_st}")
print(f"third_st: {third_st}")

# Modifying tuple elements by converting to a list and back
students = list(students)  # Convert tuple to a list
students[0] = "Panagiotis"  # Modify the first element
students = tuple(students)  # Convert the list back to a tuple

# Print the modified tuple and its type
print(students)
print(type(students))