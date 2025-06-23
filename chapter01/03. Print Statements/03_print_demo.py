# Initialize an integer, a float, and a string variable
my_int = 10       # Integer value
my_float = 5.5    # Floating point number
my_str = "Hello CF!"  # String value

# Print a header message before printing values
print("Printing comma separated values:")

# Print variables separated by space (default behavior)
print(my_int, my_float, my_str)

# Print a separator line
print("-------------------------")

# Print variables separated by a tab character
print(my_int, my_float, my_str, sep="\t")

# Print another separator line
print("-------------------------")

# Print variables separated by a tab, ending the print statement with '---' followed by a new line
print(my_int, my_float, my_str, sep="\t", end="---\n")
