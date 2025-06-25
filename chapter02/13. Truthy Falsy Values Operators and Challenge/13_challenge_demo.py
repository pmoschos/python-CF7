# Falsy - Truthy Values
# Examples of falsy values: 0, 0.0, 0j, "", [], {}, (), set(), False, None

# Define an empty dictionary and check its type
empty_dict = {}  # <class 'dict'>
print(type(empty_dict))

# Conditional expression: checking if a value lies within a range
# Example: 0 < a < 10

# Define a value for `a`
a = 5

# Using and operator
if a > 0 and a < 10:
    print("Valid num")

# Using chained comparison for the same logic
if 0 < a < 10:
    print("Valid num")

# Challenge: Modifying a tuple
students = ("Alice", "Bob", "Charlie")

# Replace the first element by converting tuple to list and back
students = tuple(["Panagiotis"] + list(students)[1:])
print(students)

# Using enumerate() for custom iteration
students = ["Alice", "Bob", "Charlie", "David"]

# Enumerate with a custom start index
for index, value in enumerate(students, start=100):
    print(f"{index} : {value}")