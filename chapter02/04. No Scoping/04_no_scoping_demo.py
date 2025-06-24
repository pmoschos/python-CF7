import random

# Initialize an empty list to store random numbers
random_numbers = []

# Use a for loop to generate 10 random integers
for _ in range(10):  # Loop runs 10 times
    num = random.randint(1, 100)  # Generate a random integer between 1 and 100
    random_numbers.append(num)  # Append the generated number to the list

# Print the generated list of random numbers
print(random_numbers)

# Find the last even number in the list
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        even = num  # Store the current even number

# Print the last number in the list (regardless of even or odd)
print(f"The last item of the list: {num}")

# Print the last even number encountered in the loop
print(f"The last 'even' item of the list: {even}")