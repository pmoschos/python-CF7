# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Using dictionary comprehension to create a dictionary of numbers and their squares
squares_dict = {number: number ** 2 for number in numbers}
# Output the result
print(squares_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Using dictionary comprehension to create a dictionary of even numbers and their squares
even_squares_dict = {number: number ** 2 for number in numbers if number % 2 == 0}
# Output the result
print(even_squares_dict) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# Returns the square of the given number
def square(number):
    """
    Return the square of the given number.
    
    Args:
    number (int): A number to be squared.
    
    Returns:
    int: The square of the number.
    """
    return number ** 2

# Using dictionary comprehension to create a dictionary of numbers and their squares
# The comprehension iterates over each number in the list 'numbers'
# For each number, it calls the 'square' function to compute the square of the number
# The number is used as the key and the square of the number as the value in the resulting dictionary
squares_dict = {number: square(number) for number in numbers}

# Output the resulting dictionary
print(squares_dict) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}