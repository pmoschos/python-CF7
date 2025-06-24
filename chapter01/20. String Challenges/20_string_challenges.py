# print the message as follows

# Challenge 1
# Printing each character of the word "Factory" incrementally repeated on each line.
# F
# aa     
# ccc    
# tttt   
# ooooo
# rrrrrr
# yyyyyyy
print("Challenge 1")
message = "Factory"
for i in range(len(message)):
    print(message[i] * (i + 1))

# Challenge 2
# Printing each character of the word "Factory" incrementally repeated,
# followed by a decreasing number of asterisks to form a right-aligned triangle.
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy
print("Challenge 2")
for i in range(len(message)):
    print(message[i] * (i + 1), end="*" * (len(message) - i - 1))
    print()

