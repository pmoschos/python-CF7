# Prompt the user to enter a username and store it in a variable
username = input(f"Enter your username: ")

# Prompt the user to enter an email address and store it in a variable
email = input("Enter your email: ")

# Using the 'or' logical operator to assign a fallback value
# If 'username' is truthy (non-empty), use it; otherwise, use the fallback value "User"
valid_user = username or "User"

# Repeat the operation to reinforce the example (this line could be omitted as it's redundant)
valid_user = username or "User"

# Use a combination of 'and' and 'or' to construct an output message
# 'email and f"your email is {email}"' evaluates to the email message if 'email' is non-empty
# If 'email' is empty, the expression after 'or' is used, asking for a valid email address
print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid email address.")))
