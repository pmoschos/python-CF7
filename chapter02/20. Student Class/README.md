# 🏗️ Python Object-Oriented Programming Demonstration 🧩

Welcome to the Python Object-Oriented Programming Demonstration! This script showcases how to define and utilize a class in Python, using a simple `Student` class as an example. It's an excellent resource for anyone new to Python or those teaching programming concepts related to object-oriented programming.

## Script Overview 📘

The script demonstrates how to define a `Student` class with attributes for a student's first name and last name. It includes methods for initializing a student object and printing student information, illustrating basic principles of object-oriented programming.

### :computer: Script Code

```python
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
```

## Key Features 🌟
- **Class Definition**: Learn how to define classes in Python, including initialization and attribute handling.
- **Object Instantiation**: Understand how to create instances of a class and utilize their attributes.
- **Method Implementation**: Discover how to implement methods within a class that perform operations on object attributes.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None required, uses standard Python capabilities.

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `20_student_class_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `20_student_class_demo.py`.
5. Run the script with: `python 20_student_class_demo.py`.

## Usage Example 📋
Execute the script to create a Student object and print its attributes. This will help you understand the practical applications of class definition and object instantiation in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*
---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>