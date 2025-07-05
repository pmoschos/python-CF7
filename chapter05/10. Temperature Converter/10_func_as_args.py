# Define a higher-order function that takes two numbers and a function as parameters
def calculator(n1, n2, operation):
    """
    A calculator function that applies a passed function (operation) to two numbers.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        operation (function): A function that takes two integers and returns an integer.

    Returns:
        int: The result of applying the operation function to n1 and n2.
    """
    try:
        # Call the operation function with the numbers
        return operation(n1, n2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' argument is a function taking two integers.")
        return None

# Define some basic operation functions
def add(no1, no2):
    """Return the sum of two numbers."""
    return no1 + no2

def subtract(no1, no2):
    """Return the difference between two numbers."""
    return no1 - no2

def multiply(no1, no2):
    """Return the product of two numbers."""
    return no1 * no2

def divide(no1, no2):
    """Return the division of two numbers."""
    if no2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return no1 / no2

# Test the calculator function
if __name__ == "__main__":
    print("Addition: ", calculator(5, 3, add))  # Output: 8
    print("Subtraction: ", calculator(5, 3, subtract))  # Output: 2
    print("Multiplication: ", calculator(5, 3, multiply))  # Output: 15
    print("Division: ", calculator(5, 3, divide))  # Output: 1.666...

    # Demonstrate error handling by passing an invalid function
    print("\nAttempting invalid operation...")
    invalid_operation = "not_a_function"
    print("Result: ", calculator(5, 3, invalid_operation))  # Outputs an error message

    # Demonstrate error handling with division by zero
    print("\nAttempting division by zero...")
    try:
        print("Result: ", calculator(5, 0, divide))
    except Exception as e:
        print(f"Caught an error: {e}")
