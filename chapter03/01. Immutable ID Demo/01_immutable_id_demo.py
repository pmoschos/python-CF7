def print_id(variable_name, variable):
    """
    Prints the id of the given variable.

    Args:
    variable_name (str): The name of the variable as a string.
    variable: The variable whose id is to be printed.
    """
    print(f"id({variable_name}) = {id(variable)}")

def main():

    # Interning (όπως το String pool της Java)

    # Define integer variables
    a = 10
    b = 10

    # Define string variables
    str1 = "CF"
    str2 = 'CF'

    # Print the ids of the variables
    print_id("a", a)
    print_id("b", b)

    print_id("str1", str1)
    print_id("str2", str2)

if __name__ == "__main__":
    main()
