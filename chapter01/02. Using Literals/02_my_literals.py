# Initialize three integer variables in different number systems
num1 = 10           # Decimal format
num2 = 0b1010       # Binary format
num3 = 0x000A       # Hexadecimal format

# Initialize string variables in various quotation styles
str1 = 'CF'         # Single quotes for short strings
str2 = "CF"         # Double quotes, interchangeable with single quotes for strings
str3 = 'Cod\
ing'                # Line continuation character used to extend the string across the newline

# Multi-line string using triple single quotes
str4 = '''Hello
Coding
Factory'''

# Multi-line string using triple double quotes
str5 = """Hello
again!
"""

# Boolean variable initialized as True
my_bool = True

# Print the initialized variables to observe their values and types
print(num1, num2, num3, str1, str2, str3, my_bool)
print("----------------")

# Display text to categorize output
print("Types:")

# Print the data types of each variable to show the distinction between them
print(type(num1))     # Should show <class 'int'>
print(type(num2))     # Should show <class 'int'>
print(type(num3))     # Should show <class 'int'>
print(type(str1))     # Should show <class 'str'>
print(type(str2))     # Should show <class 'str'>
print(type(str3))     # Should show <class 'str'>
print(type(str4))     # Should show <class 'str'>
print(type(str5))     # Should show <class 'str'>
print(type(my_bool))  # Should show <class 'bool'>

