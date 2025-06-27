def main():
    # Prompt the user to input an integer and convert it to an int
    n = int(input("Please insert an int: "))

    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1

    # Iterate from 2 to n to calculate the nth Fibonacci number
    for i in range(2, n + 1):
        # Store the current value of 'a' in a temporary variable
        temp = a
        # Update 'a' to be the value of 'b'
        a = b
        # Update 'b' to be the sum of the old 'a' (now in 'temp') and 'b'
        b = temp + b

    # Print the nth Fibonacci number
    print(f"The {n}th Fibonacci number is {b}")

# If this script is being run directly (as opposed to being imported as a module),
# call the main function
if __name__ == "__main__":
    main()
