class Student:
    """
    A class that represents a student with a first name and a last name.

    Attributes:
        firstname (str): The first name of the student.
        lastname (str): The last name of the student.
    """

    def __init__(self, firstname: str, lastname: str):
        """
        Initialize a Student object with the provided first name and last name.

        Args:
            firstname (str): The first name of the student.
            lastname (str): The last name of the student.
        """
        self.firstname = firstname
        self.lastname = lastname

def main():
    # Create a Student object
    student = Student("Bob", "Marley")

    # Print the attributes of the Student object
    print("First Name:", student.firstname)
    print("Last Name:", student.lastname)

if __name__ == "__main__":
    main()