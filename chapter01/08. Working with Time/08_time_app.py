# Constants for converting units of time
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

# Prompt the user to enter the total number of seconds
total_seconds = int(input("Enter the number of seconds: "))
# Example conversion: 105310 seconds is equal to: 1 day, 5 hours, 15 minutes, 10 seconds

# Calculate the number of days from the total seconds and the remainder
days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

# Calculate the number of hours from the remaining seconds
hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR  # Update the seconds_remaining by applying modulus

# Calculate the number of minutes from the updated remaining seconds
minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE  # Further reduce the remaining seconds

# The final value of seconds_remaining is the number of seconds
seconds = seconds_remaining

# Display the results in a clear, formatted way
print(f"{total_seconds} seconds is equal to:")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
