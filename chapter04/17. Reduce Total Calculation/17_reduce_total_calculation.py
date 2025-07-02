from functools import reduce

# List of numbers
my_ints = [1, 2, 3, 4, 5]

# Using reduce to compute the product of all elements in the list
# Lambda function takes two arguments x and y and returns their product
result = reduce(lambda x, y: x * y, my_ints) # return a result: 1 * 2 * 3 * 4 * 5

# An initial value of 1 is provided to handle the empty list scenario gracefully
result = reduce(lambda x, y: x * y, my_ints, 1)

# Printing the result of the product calculation
print("Result:", result)
