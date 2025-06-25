def print_cities(*cities):
    # Check if any cities are provided
    if not cities:
        print("No cities provided")
    else:
        # Join and print the cities separated by commas
        print("Cities:", ", ".join(cities))

def main():
    # Example calls to print_cities
    print_cities("Athens", "London", "Paris")  # Cities: Athens, London, Paris
    print_cities("Athens")  # Single city
    print_cities()  # No cities provided

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()