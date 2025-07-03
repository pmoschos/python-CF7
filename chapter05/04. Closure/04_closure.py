def department_id_generator(department):
    """
    Generate unique IDs for students based on department.

    Parameters:
    department (str): The name of the department.

    Returns:
    function: A function that generates unique IDs for the given department.
    """
    last_id = 0  # Initialize the last_id to zero

    def generate_id():
        """
        Generate a unique ID for a student in the department.

        Returns:
        tuple: A tuple containing the unique ID as a string and the last_id as an integer.
        """
        nonlocal last_id  # Declare last_id as nonlocal to modify it within the nested function
        last_id += 1  # Increment the last_id
        return f"{department}-{last_id}", last_id  # Return the formatted ID and last_id
    
    return generate_id  # Return the nested function

def main():
    # Create ID generators for Python and Android departments
    python_id_gen = department_id_generator("Python")
    android_id_gen = department_id_generator("Android")

    # Generate and print IDs using the Python ID generator
    print(python_id_gen())  # Expected output: ('Python-1', 1)
    print(python_id_gen())  # Expected output: ('Python-2', 2)

    # Generate and print IDs using the Android ID generator
    print(android_id_gen())  # Expected output: ('Android-1', 1)

    # Generate and print another ID using the Python ID generator
    print(python_id_gen())  # Expected output: ('Python-3', 3)

if __name__ == "__main__":
    main()
