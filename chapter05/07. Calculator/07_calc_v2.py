import functools

def calculate(args: list[float]) -> dict:
    """
    Generate functions to perform arithmetic operations on a list of numbers.

    Parameters:
    args (list of float): List of numbers to perform operations on.

    Returns:
    dict: A dictionary of functions for addition, subtraction, multiplication,
          and average.
    """
    def plus() -> float:
        """Return the sum of the numbers in the list."""
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus() -> float:
        """Return the result of subtracting the numbers in the list."""
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul() -> float:
        """Return the product of the numbers in the list."""
        return functools.reduce(lambda x, y: x * y, args)

    def average() -> float:
        """Return the average of the numbers in the list."""
        return sum(args) / len(args)

    return {
        "add": plus,
        "subtract": minus,
        "multiply": mul,
        "average": average,
    }

def main() -> None:
    """
    Main function to demonstrate the usage of calculate.
    """
    print("Welcome to the Arithmetic Operations App!")
    args = [26, 5, 4, 3, 2, 1]  # Example list of numbers
    operations = calculate(args)

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Average")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        match choice:
            case 1:
                print("Addition result:", operations["add"]())
            case 2:
                print("Subtraction result:", operations["subtract"]())
            case 3:
                print("Multiplication result:", operations["multiply"]())
            case 4:
                print("Average:", operations["average"]())
            case 5:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
