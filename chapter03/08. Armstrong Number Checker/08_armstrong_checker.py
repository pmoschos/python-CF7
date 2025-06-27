def is_armstrong_number(n):
    """
    Checks if a number is an Armstrong number.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return n == total

def main():

    # Example: 371 = 3^3 + 7^3 + 1^3

    try:
        num = int(input("Please insert an int: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

if __name__ == "__main__":
    main()
