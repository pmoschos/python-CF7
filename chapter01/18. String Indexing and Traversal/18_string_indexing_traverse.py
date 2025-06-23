# In Python, there is no specific 'char' data type like in some other languages
# Εvery character is treated as a string of length one.

character = 'a'  # Defined as a string with a single character

# Print the character and its data type using formatted string literals (f-strings)

print(f"'{character}' is type of: {type(character)}")

# Output will show that the type of 'character' is <class 'str'>, indicating it's a string

# Define a string variable
message = "Coding Factory"

# Print individual characters using indexing (zero-indexed)
print(message[0])  # 'C'
print(message[1])  # 'o'
print(message[2])  # 'd'
print(message[3])  # 'i'
print(message[4])  # 'n'
print(message[5])  # 'g'

# Strings in Python are immutable, which means you cannot change an existing string directly
# The following line, if uncommented, would result in a TypeError because strings cannot be modified
# message[0] = 'c'

# Use len() to get the number of characters in the string
print(f"Number of letters inside the {message}: {len(message)}")  # Outputs the length of the message

# Iterate over each character in the string using a simple for-loop
for char in message:
    print(char)  # Prints each character on a new line

# The range function generates a sequence of numbers, which by default starts from 0 and goes up to n-1
for i in range(10):
    print(i)  # Prints numbers 0 to 9

# Iterate over the string by index using a for-loop with range based on the length of the message
for i in range(len(message)):
    print(message[i], end=" ")  # end=" " keeps the output on the same line
print()  # Print a newline at the end

# Numeric operations with strings
number = 12345678
number_str = str(number)

# Print individual characters using indexing
print("\nPrint the variable number_str per char\n")
print(int(number_str[0]))  # '1'
print(int(number_str[1]))  # '2'
print(number_str[2])  # '3'
print(number_str[3])  # '4'
print(number_str[4])  # '5'
print(number_str[5])  # '6'
print(number_str[6])  # '7'
print(int(number_str[7]))  # '8'
print("... end of variable number_str\n")

# Perform numeric operations on string-converted digits
print("\n-----\nThe sum of the first [0] and second digit [1] is:", int(number_str[0]) + int(number_str[1]), ".")
print("The sum of the first [0] and eighth digit [7] is:", int(number_str[0]) + int(number_str[7]), ".  \n-----\n")