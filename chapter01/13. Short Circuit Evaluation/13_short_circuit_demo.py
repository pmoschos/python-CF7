# Define a string variable for the name
name = "Bob"

# Demonstrate the use of the `or` logical operator for variable assignment
print("====== or ======")
# Use `or` to assign "User" to valid_user if the left-hand side (None in this case) is falsy
valid_user = None or "User"
# Output: Hello User
print("Hello", valid_user)
print()

# If `name` has a truthy value, it will be assigned to valid_user; otherwise, "User" would be assigned
valid_user = name or "User"
# Output: Hello Bob
print("Hello", valid_user)
print()

# Demonstrate the use of the `and` logical operator for conditional checking
print("====== and ======")

# Define a string variable for the email
email = "bob@example.com"
# Use `and` to check that email is not empty and assign the email to valid_email if it's true
valid_email = email and email != ""
# Output: Valid Email: bob@example.com
print("Valid Email:", valid_email)

# EXTRA: Conditional output based on the value of valid_email
if valid_email:
    # If valid_email is truthy, print a greeting and the email address
    print(f"Hello {valid_user}, your email is {email}")
else:
    # If valid_email is falsy, prompt the user to provide a valid email address
    print(f"Hello {valid_user}, please provide a valid email address.")
