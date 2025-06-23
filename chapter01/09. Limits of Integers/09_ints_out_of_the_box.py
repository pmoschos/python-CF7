# Initialize two integer variables
a = 10
b = 20

# Perform addition and store the result in a variable
result = a + b
# Print the result of the addition
print("a + b =", result)

# Print a separator line for clarity in output
print("---------")

# Display the data type of variable 'a'
print("Type of a:", type(a))

# Using the magic method __add__() to perform the addition
# Magic methods in Python are special methods which add "magic" to your classes.
# __add__ is one of these magic methods that allows the object of the class to use the + operator.
magic_result = a.__add__(b)
# Print the result obtained using the magic method
print("a + b =", magic_result)

