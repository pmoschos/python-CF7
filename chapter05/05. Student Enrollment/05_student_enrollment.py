def enroll_students(*students, min_grade=50, department="Computer Science", **kwargs):
    """
    Enroll students in a department with a minimum grade requirement and additional information.

    Parameters:
    *students (str): Names of students to enroll.
    min_grade (int, optional): Minimum grade required for enrollment. Defaults to 50.
    department (str, optional): Department for enrollment. Defaults to "Computer Science".
    **kwargs (dict): Additional keyword arguments for extra information.
    """
    # Print the minimum grade required for enrollment
    print(f"Min grade: {min_grade}")
    # Print the department for enrollment
    print(f"Department: {department}")

    # Print the list of enrolled students
    print("\nEnrolled Students")
    for student in students:
        print(f" - {student}")
    
    # Print any additional information provided through keyword arguments
    print("\nAdditional Information")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("--- End of enrollment ---")
    print()

def main():
    """
    Main function to demonstrate the usage of enroll_students.
    """
    # Enroll Alice and Bob in the default department (Computer Science) with the default min grade
    enroll_students("Alice", "Bob")
    print("-----------")

    # Enroll Helen, Carol, and Nick with additional keyword arguments
    enroll_students("Helen", "Carol", "Nick", academic_year=2023, semester="Fall")
    print("-----------")

    # Enroll Dalton with overridden default values for min_grade and department
    enroll_students("Dalton", min_grade=40, department="Theater")
    print("-----------")

    # Enroll students John and Dave with both overridden defaults and additional kwargs
    enroll_students("John", "Dave", min_grade=70, department="Maths", academic_year=2023, semester="Spring")

if __name__ == "__main__":
    main()
