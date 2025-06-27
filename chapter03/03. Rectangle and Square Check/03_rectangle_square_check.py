def is_square(length, width):
    """
    Checks if a rectangle is a square.

    Args:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.

    Returns:
    bool: True if the rectangle is a square, False otherwise.
    """
    return length == width

def main():
    # Get user input for the length and width of the rectangle
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
    except ValueError:
        print("Invalid input. Please enter valid integers for length and width.")
        return

    # Check if the rectangle is a square and print the result
    if is_square(length, width):
        print("The rectangle is a square.")
    else:
        print("The rectangle is not a square.")

if __name__ == "__main__":
    main()
