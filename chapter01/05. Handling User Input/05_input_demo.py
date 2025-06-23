# Request user's name via input and store it in a variable
name = input("Please enter your name: ")
# Print a personalized greeting using the inputted name
print("Hello, " + name + "!")

# Request user's year of birth and convert it directly to an integer
# This prevents type conversion errors later in the code
year_of_birth = int(input("Please enter the year of your birth: "))

# Calculate and print the user's age using the current year minus the year of birth
# The conversion to int was originally done after input, which is now refactored to be immediate
print("You are", 2024 - year_of_birth, "years old.")   

# Request the user's height in centimeters and convert it to a float for precision
height = float(input("Please enter your height in cm: "))
# Convert height from centimeters to meters and print it
print("You are", height / 100, "meters tall")


