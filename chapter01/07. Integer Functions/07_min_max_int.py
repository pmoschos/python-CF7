import sys

# Largest integer 
max_int = sys.maxsize
print("Max int:", max_int)

# Smallest integer 
min_int = -sys.maxsize - 1
print("Min int:", min_int)

# For a 64-bit system, you would get:
# Max size: 9223372036854775807
# Max int: 9223372036854775807
# Min int: -9223372036854775808

# For a 32-bit system, you would get:
# Max size: 2147483647
# Max int: 2147483647
# Min int: -2147483648