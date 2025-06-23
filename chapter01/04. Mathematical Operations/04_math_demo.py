import math  # Import the math module to access mathematical constants and functions

# Define string and integer variables
name = "Alice"
age = 20

# Print a simple string
print("CF")
# Print the mathematical constant PI from the math module
print("PI =", math.pi)

# Demonstrate string concatenation
print("String Concatenation")
# This line would cause a TypeError because you cannot concatenate string and integer directly
# print(name + " is" + age + " years old.")  # Incorrect way, commented out
print(name + " is " + str(age) + " years old.")  # Correct by converting age to a string
print("-------------------------")

# Demonstrate old Python 2 style string formatting using the % operator
print("Python 2 style")
print("PI = %6.2f" % math.pi)  # Format PI to two decimal places with padding
print("%s is %d years old" % (name, age))  # Use placeholders for string and integer
print("-------------------------")

# Demonstrate Python 3 style string formatting using the str.format() method
print("Python 3 style using string format")
print("Age is {0:2d}".format(age))  # Format age with 2-digit padding
print("PI = {0:.3f}".format(math.pi))  # Format PI to three decimal places
# Explanation of the '0' in format: It refers to the first argument passed to format()
print("PI = {0:.3f} and age = {1}".format(math.pi, age))  # Multiple placeholders
print("-------------------------")

# Print combining text and variables using format and specifying the print end character
print("{0} is {1}".format(name, age), end=" ")
print("years old.")

# Using string formatting for alignment and padding
print("{0:*^10}:{1:>20}".format(name, age))  # Center name with asterisks, right-align age
print("{0:*^10}:{1:<20}".format(name, age), end="|")  # Left-align age, end print with '|'
print("-------------------------")

# Demonstrate modern Python 3 style string interpolation using f-strings
print("Python 3 style using f-strings")
print(f"{name} is {age} years old.")  # Embed expressions inside string literals directly
