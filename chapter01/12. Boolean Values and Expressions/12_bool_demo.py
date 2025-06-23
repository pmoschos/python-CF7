# Define Boolean variables
a = True
b = False

# Print the type and value of each Boolean variable
print(type(a), a)
print(type(b), b)

# Demonstrate the logical OR operation
# The OR operation short-circuits; it stops evaluating once the truth value is determined.
# Since `a` is True, `b` is not evaluated in this case.
result = a or b  # `b` is not evaluated because `a` is `True`
print(result)  # Output: True

# Show how Booleans behave in arithmetic contexts
# Booleans in Python are a subclass of integers. True is 1, and False is 0.
print("True + True = ", True + True)  # Output will be 2, demonstrating arithmetic addition of Booleans
