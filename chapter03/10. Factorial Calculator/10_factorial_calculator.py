def calculate_factorial(n):
    """
    Calculates the factorial of a given number.
    
    Args:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the number.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    try:
        n = int(input("Please insert a non-negative integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return
    
    factorial = calculate_factorial(n)
    
    print(f"{n}! = {factorial:,}")

if __name__ == "__main__":
    main()
