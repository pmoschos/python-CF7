# ✍️ Enroll Students Script 🏫

Welcome to the Enroll Students Script! This script demonstrates how to enroll students in a department with a minimum grade requirement and additional information using variable-length arguments, default values, and keyword arguments.

## Script Overview 📘

The script defines a function `enroll_students` which accepts student names, a minimum grade requirement, a department, and additional keyword arguments. It prints out the enrollment details including the list of students, the department, the minimum grade required, and any additional information provided.

### :computer: Script Code

```python
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
```

# Enroll Students Script

Welcome to the Enroll Students Script! This script demonstrates how to enroll students in a department with a minimum grade requirement and additional information using variable-length arguments, default values, and keyword arguments.

## Key Features 🌟

- **Variable-Length Arguments**: Learn how to define and use functions with variable-length argument lists in Python.
- **Default Parameters**: Discover how to use default values for function parameters.
- **Keyword Arguments**: Understand how to use keyword arguments to pass additional information to a function.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `05_student_enrollment.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `05_student_enrollment.py`.
5. Run the script with: `python 05_student_enrollment.py`.

## Usage Example 📋

Execute the script to see how variable-length arguments, default parameters, and keyword arguments can be used to enroll students in a department. The script will demonstrate different ways of calling the `enroll_students` function with various parameters and keyword arguments.

## 📢 Stay Updated

Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License

🔐 This project is protected under the MIT License.

## Contact 📧

Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
