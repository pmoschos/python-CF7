# Original list of numbers
list_of_ints = [1, 2, 3, 4, 5, 6, 7]

# 1. Using list comprehension to square each number in the list
squared_list_comprehension = [number ** 2 for number in list_of_ints]

# Printing the results
print(f"Squared numbers (list comprehension): {squared_list_comprehension}")


# 2. Using map() with a lambda function to square each number in the list
squared_map_lambda = list(map(lambda number: number ** 2, list_of_ints))

# Printing the results
print(f"Squared numbers (map with lambda): {squared_map_lambda}")


# 3. This function takes an integer and returns its square.
def square_function(num):
    return num ** 2

# Printing the results using a list comprehension with a named function
# The condition `if number == 100` will filter out all numbers since none are 100
filtered_squared_func_results = [square_function(number) for number in list_of_ints if number == 100]
print(f"Squared numbers with filter (list comprehension with function): {filtered_squared_func_results}")


# 4. Using map() with the named function to square each number in the list
squared_map_function = list(map(square_function, list_of_ints))

# Printing the results
print(f"Squared numbers (map with function): {squared_map_function}")


# 5. Filtering and squaring only even numbers using list comprehension
filtered_squared_list_comprehension = [number ** 2 for number in list_of_ints if number % 2 == 0]

# Printing the results
print(f"Filtered and squared numbers (list comprehension): {filtered_squared_list_comprehension}")


# 6. Filtering and squaring only even numbers using filter() and map()
filtered_squared_map_filter = list(map(square_function, filter(lambda x: x % 2 == 0, list_of_ints)))

# Printing the results
print(f"Filtered and squared numbers (map and filter): {filtered_squared_map_filter}")
