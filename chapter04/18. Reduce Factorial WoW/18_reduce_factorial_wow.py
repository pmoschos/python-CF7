from functools import reduce

# Prompt the user to input an integer for which the factorial is to be calculated
n = int(input("Give an int to calc facto: "))

# Use the reduce function to calculate the factorial of the number
# The reduce function applies a rolling computation to sequential pairs of values in a range from 1 to n+1
# The lambda function provided to reduce takes two arguments x and y, multiplying them together
# Since range(1, n+1) generates numbers from 1 to n, this effectively calculates the product of all integers from 1 to n, which is the factorial

# Example for reduce()
# reduce(lambda x, y: x * y, range(1, 5 + 1))
# First step: x = 1, y = 2 (Result: 1 * 2 = 2)
# Second step: x = 2 (result of previous step), y = 3 (Result: 2 * 3 = 6)
# Third step: x = 6 (result of previous step), y = 4 (Result: 6 * 4 = 24)
# Fourth step: x = 24 (result of previous step), y = 5 (Result: 24 * 5 = 120)
result = reduce(lambda x, y: x * y, range(1, n + 1))

# Output the result to the user, formatting it as n! = result
print(f"{n}! = {result}")


# Modified lambda function to print intermediate results
def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

result = reduce(print_and_multiply, range(1, n + 1))

print(f"Final result: {result}")


# Use reduce with a lambda function that includes a print statement
result = reduce(lambda x, y: print(f"{x} * {y} = {x * y}") or x * y, range(1, n + 1))
print(f"Final result: {result}")