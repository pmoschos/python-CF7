# Type Annotations for Parameters (a: float | int, b: float | int):
# Return Type Annotation (-> float | int)
def my_add(a: float | int, b: float | int) -> float | int:
    """
    Adds two numbers and returns the result.

    Args:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

    Returns:
    int | float: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        # return 0
        # raise TypeError
        raise TypeError("Both a and b must be integers or floats.")
    return a + b

def main():
    # Testing the function
    print(my_add(10, 20))          # Outputs: 30
    print(my_add(5, 8.3))          # Outputs: 13.3
    try:
        print(my_add("Hello ", "Coding Factory"))  # This call should raise an error
    except TypeError as e:
        print(e)  # Outputs: Both a and b must be integers or floats.
    
    print("Annotations:", my_add.__annotations__)
    print("Docs:", my_add.__doc__)

    print("--------------------------------")

    help(my_add)

if __name__ == "__main__":
    main()
