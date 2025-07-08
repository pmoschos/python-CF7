def main():
    """
    Main function to demonstrate tuple properties and mutability of its elements.
    """
    # Creating a tuple
    g = 1, 2, 3, 5

    # Printing the type of g to show that it is a tuple
    print("Type of g:", type(g))  # Output: <class 'tuple'>

    # Tuple mutability test
    # Tuples are unmodifiable, but if they contain mutable elements, those elements can be changed.
    my_tuple = (1, 2, [3, "CF"], "Hello")

    # Attempt to change an unmodifiable element of the tuple (this will raise an error)
    try:
        my_tuple[2] = [1, 2, 3]
    except TypeError as e:
        print(f"Error: {e}")  # Output: 'tuple' object does not support item assignment

    # Accessing and printing the second element of the tuple
    print("Second element of my_tuple:", my_tuple[1])  # Output: 2

    # Printing the id and value of each item in the tuple before modification
    print("\nBefore modification:")
    for item in my_tuple:
        print(id(item), ":", item)

    # Modifying the first element of the list inside the tuple
    my_tuple[2][0] = 300

    # Printing the modified tuple
    print("\nAfter modification:")
    print("Modified my_tuple:", my_tuple)  # Output: (1, 2, [300, 'CF'], 'Hello')

    # Printing the id and value of each item in the tuple after modification
    print("\nIDs and values after modification:")
    for item in my_tuple:
        print(id(item), ":", item)

if __name__ == "__main__":
    main()
