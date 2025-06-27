def print_id(variable_name, variable):
    """
    Prints the id of the given variable.

    Args:
    variable_name (str): The name of the variable as a string.
    variable: The variable whose id is to be printed.
    """
    print(f"id({variable_name}) = {id(variable)}")

def main():
    # Define the original list
    original_list = [1, 2]

    # Assign the original list to a new variable
    new_list = original_list

    # Print the ids of the lists
    print_id("original_list", original_list)
    print_id("new_list", new_list)

    # Check if both variables point to the same object
    print(f"original_list is new_list: {original_list is new_list}")

    # Print the id of a new list with the same elements
    temp_list = [1, 2]
    print_id("temp_list", temp_list)

if __name__ == "__main__":
    main()
