# Request the user's name and store it in a variable
name = input("Please enter your name: ")

# Request the user's age, converting the input directly to an integer
age = int(input("Please enter your age: "))

# Request the user's height in meters, converting the input directly to a float for precision
height = float(input("Please enter your height in meters: "))

# Request a yes/no answer to determine if the user is a student, converting to lowercase and comparing to 'yes'
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'

# Print a formatted greeting using the user's name
print("\nHello, {}!".format(name))

# Condition to check if the user is a student and print the corresponding status
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
    
# Print the user's age and height, formatting the height to two decimal places
print("Your age is {}, and your height is {:.2f} meters.".format(age, height))


