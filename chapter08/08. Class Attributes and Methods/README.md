# 🎓 Student Class Demonstration Script 🧑‍🏫

Welcome to the Student Class Demonstration Script! This script showcases how to define a Python class with attributes and methods to manage student information effectively. The script includes class-level attributes, instance methods for updating and displaying student information, and functions for exploring class-level attributes and methods dynamically.

## Script Overview 📘

The script defines a `Student` class to encapsulate the properties of a student, such as their name, age, and grade. It also includes methods to:
- Update the grade of a student.
- Check if a student is an adult.
- Display a student's information.

Additionally, the script dynamically explores and displays class attributes and methods.

### :computer: Script Code

```python
class Student:
    school_name = "Example High School"  # Class attribute

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def update_grade(self, new_grade):
        """Updates the student's grade."""
        self.grade = new_grade
        print(f"Grade updated to {self.grade}")

    def is_adult(self):
        """Checks if the student is an adult (age >= 18)."""
        return self.age >= 18

    def display_info(self):
        """Displays the student's information."""
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


print(Student.__dict__.items())

print("\nClass Attributes and Methods:")
print("-" * 30)
for attr_name, attr_value in Student.__dict__.items():
    print(f"{attr_name:<15}: {attr_value}")

print("\nClass Methods:")
print("-" * 30)
for attr_name, attr_value in Student.__dict__.items():
    if callable(attr_value):
        print(f"{attr_name:<15}: {attr_value}")

print("\nClass Attributes:")
print("-" * 30)
for attr_name, attr_value in Student.__dict__.items():
    if not callable(attr_value) and not attr_name.startswith("__"):
        print(f"{attr_name:<15}: {attr_value}")
```

## Key Features 🌟

- **Class Definition**: Learn how to define classes with class-level and instance attributes.
- **Dynamic Exploration**: Understand how to explore class-level attributes and methods dynamically using `__dict__`.
- **Instance Methods**: Discover how to add functionality such as grade updates and adulthood checks to class instances.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses built-in Python functionalities).

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `08_class_attrs_methods.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `08_class_attrs_methods.py`.
5. Run the script with: `python 08_class_attrs_methods.py`.

## Usage Example 📋

Execute the script to:
1. See class attributes and methods dynamically listed.
2. Learn how to interact with instance attributes and methods.

The script demonstrates key concepts of Python OOP and class functionality.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>

