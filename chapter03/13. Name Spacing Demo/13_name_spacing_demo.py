def name_spacing(num: int):
    """
    Prints each character of the given name separated by a specified number of spaces.
    
    Args:
    num (int): The number of spaces to insert between each character.
    """
    if not isinstance(num, int):
        print("The number of spaces must be an integer.")
        return

    if num < 0:
        print("The number of spaces must be a non-negative integer.")
        return

    name = input("Please give a name: ").strip()
    
    if not name:
        print("No name provided.")
        return

    # Create the spaced string and print it
    spaced_name = (' ' * num).join(name)
    print(spaced_name)

def main():
    # Example usage
    try:
        num = int(input("Enter the number of spaces between characters: "))
        name_spacing(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of spaces.")

if __name__ == "__main__":
    main()


