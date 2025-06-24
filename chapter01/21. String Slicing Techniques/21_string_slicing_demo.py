s = "Coding Factory"

# Single character slicing using positive indexing
s1 = s[7]  # 'F', the character at index 7

# Slicing a substring from the beginning up to (but not including) index 6
s2 = s[:6]  # 'Coding'

# Slicing a substring from index 7 to the end of the string
s3 = s[7:]  # 'Factory'

# Slicing the whole string
s4 = s[:]  # 'Coding Factory'
# Alternatively, s4 = s[::] would yield the same result

# Negative slicing
# Slicing from the start up to (but not including) the last character
s5 = s[:-1]  # 'Coding Factor'

# Slicing from the start up to (but not including) the second to last character
s6 = s[:-2]  # 'Coding Facto'

# Print the results of the slicing operations
print(s1)  # Outputs: F
print(s2)  # Outputs: Coding
print(s3)  # Outputs: Factory
print(s4)  # Outputs: Coding Factory
print(s5)  # Outputs: Coding Factor
print(s6)  # Outputs: Coding Facto

# Reversing the string using slicing
r_s = s[::-1]  # 'yrotcaF gnidoC'
print(r_s)  # Outputs: yrotcaF gnidoC

# Slicing from index 7 to index 7, which results in an empty string
s_q = s[7:7]  # ''
print(s_q)  # Outputs: (an empty line)
