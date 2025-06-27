def compare_lists(list1, list2):
    """
    Compares two lists for identity and equality.

    Args:
    list1 (list): The first list to compare.
    list2 (list): The second list to compare.

    Returns:
    None
    """
    # Check if the lists are the same object (identity)
    print(f"{list1} is {list2}: {list1 is list2}")

    # Check if the lists have the same contents (equality)
    print(f"{list1} == {list2}: {list1 == list2}")

def main():

    # Hint: when I have not overloaded the magic method for equality (__eq__()) 
    # then with == they are compared using their id's (identity)

    # Define the lists
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    # Compare the lists
    compare_lists(my_list, your_list)

if __name__ == "__main__":
    main()
