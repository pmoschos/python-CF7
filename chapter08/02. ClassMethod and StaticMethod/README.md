# 🧑‍💼 Understanding @classmethod and @staticmethod with Employee Class 📚

This Python script demonstrates the usage of `@classmethod` and `@staticmethod` in the context of an `Employee` class. It showcases how these methods differ and their specific use cases.

---

## Script Overview 📘

### Class Definition: `Employee`

1. **Attributes**:
   - `_total_employees`: A class-level variable tracking the total number of employees created.
   - `firstname`, `lastname`, `salary`: Instance-level attributes for employee details.

2. **Instance Methods**:
   - `full_name`: Returns the full name of the employee.
   - `apply_raise`: Applies a percentage raise to the employee's salary.

3. **Class Methods**:
   - `total_employees`: Returns the total number of employees created.

4. **Static Methods**:
   - `calculate_bonus`: Calculates the annual bonus based on the salary and a bonus percentage.

### :computer: Script Code

```python
class Employee:
    _total_employees = 0  # This is a class variable

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        Employee._total_employees += 1  # Increment the class variable

    @classmethod
    def total_employees(cls):
        """
        Class method to get the total number of employees created.
        """
        return cls._total_employees

    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        """
        Static method to calculate the annual bonus based on salary and bonus percentage.
        """
        return salary * (bonus_percentage / 100)

    def full_name(self):
        """
        Instance method to return the full name of the employee.
        """
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self, raise_percentage):
        """
        Instance method to apply a raise to the employee's salary.
        """
        self.salary += self.salary * (raise_percentage / 100)
        return self.salary

def main():
    # Creating employee instances
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Jane", "Smith", 60000)

    # Getting the total number of employees created
    total_emps = Employee.total_employees()
    print(f"Total employees created: {total_emps}")  # Output: Total employees created: 2

    # Calculating annual bonus
    bonus = Employee.calculate_bonus(emp1.salary, 10)
    print(f"Annual bonus for {emp1.full_name()}: {bonus}")  # Output: Annual bonus for John Doe: 5000.0

    bonus = Employee.calculate_bonus(emp2.salary, 15)
    print(f"Annual bonus for {emp2.full_name()}: {bonus}")  # Output: Annual bonus for Jane Smith: 9000.0

    # Applying raises
    emp1_new_salary = emp1.apply_raise(5)
    print(f"New salary for {emp1.full_name()} after a 5% raise: {emp1_new_salary}")  # Output: New salary for John Doe after a 5% raise: 52500.0

    emp2_new_salary = emp2.apply_raise(10)
    print(f"New salary for {emp2.full_name()} after a 10% raise: {emp2_new_salary}")  # Output: New salary for Jane Smith after a 10% raise: 66000.0

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Class-Level Operations**:
  - Tracks and returns the total number of employees using a class method.
- **Utility Functionality**:
  - Provides a static method to calculate bonuses without requiring instance or class context.
- **Instance-Level Modifications**:
  - Updates individual employee salaries and provides their full names.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses Python’s standard library).

---

## Installation and Setup 🚀

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `02_class_static_methods.py`.
3. Run the script:

   ```bash
   python 02_class_static_methods.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Total employees created: 2
Annual bonus for John Doe: 5000.0
Annual bonus for Jane Smith: 9000.0
New salary for John Doe after a 5% raise: 52500.0
New salary for Jane Smith after a 10% raise: 66000.0
```

---

## 📲 Contact and Contribution

### Contact 📧
- **Author**: Panagiotis Moschos
- **Email**: pan.moschos86@gmail.com
- **GitHub**: [pmoschos](https://github.com/pmoschos)

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

