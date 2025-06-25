def print_cities(*cities: str, separator: str = ", ") -> None:
    """
    Print a list of cities separated by a specified separator.

    Parameters:
    *cities (str): A variable number of city names to be printed.
    separator (str): A string used to separate the cities in the output. Default is ', '.
    """
    if not cities:
        print("No cities provided. Please specify at least one city.")
    else:
        print("Cities:", separator.join(cities))

def main() -> None:
    """
    Demonstrates various ways to call the print_cities function.
    """
    # Calling the print_cities function with different inputs
    print("Demonstrating print_cities function:")
    print_cities("Athens", "Paris", "London")
    print_cities("London")
    print_cities("New York", "Tokyo", "Berlin", "Sydney")
    print_cities()

    # Custom separator example
    print("\nUsing a custom separator:")
    print_cities("Athens", "Paris", "London", separator=" | ")

    # Edge case: No cities provided
    print("\nNo cities example:")
    print_cities()

if __name__ == "__main__":
    main()
