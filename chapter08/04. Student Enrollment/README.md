# 🎓 Student Management System Script 📊

This Python script demonstrates a comprehensive student management system. It includes features to enroll and drop courses, calculate student age, and manage student records efficiently.

---

## Script Overview 📘

### Class Definition: `Student`

1. **Attributes**:
   - `student_id`: A unique identifier for each student.
   - `name`: The student's name.
   - `date_of_birth`: The student's date of birth (as a `datetime.date` object).
   - `courses`: A list of courses the student is enrolled in.
   - `enrollment_date`: The date the student was enrolled.
   - `student_count`: A class-level attribute to track the total number of students.

2. **Methods**:
   - `calculate_age`: Calculates and returns the student's age based on the current date.
   - `enroll_course`: Adds a new course to the student's list of courses.
   - `drop_course`: Removes a course from the student's list of courses.
   - `get_student_info`: Returns a dictionary with all student details.
   - `__del__`: Updates the total student count when a student record is deleted.

### :computer: Script Code

```python
from datetime import date, timedelta

class Student:
    """Class to represent a student in a school or university system."""
    student_count = 0

    def __init__(self, student_id, name, date_of_birth, courses=None):
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth  # Expecting a `datetime.date` object
        self.courses = courses if courses else []  # List of enrolled courses
        self.enrollment_date = date.today()
        Student.student_count += 1
        print(f"Student {self.name} (ID: {self.student_id}) enrolled on {self.enrollment_date}. "
              f"Total students: {Student.student_count}")

    def calculate_age(self):
        """Calculates and returns the student's age."""
        today = date.today()
        age = today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
        return age

    def enroll_course(self, course_name):
        """Enrolls the student in a new course."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} has been enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def drop_course(self, course_name):
        """Drops a course for the student."""
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{self.name} has dropped {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def get_student_info(self):
        """Returns a dictionary with all student details."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.calculate_age(),
            "enrollment_date": self.enrollment_date,
            "courses": self.courses,
        }

    def __del__(self):
        Student.student_count -= 1
        print(f"Student {self.name} (ID: {self.student_id}) record deleted. "
              f"Total students: {Student.student_count}")

# Example usage
def manage_students():
    # Creating student instances
    student1 = Student("S001", "Alice", date(2002, 5, 15))
    student2 = Student("S002", "Bob", date(2001, 8, 22), ["Mathematics", "Physics"])

    # Enrolling in courses
    student1.enroll_course("Mathematics")
    student1.enroll_course("Computer Science")
    student1.enroll_course("Mathematics")  # Attempt duplicate enrollment

    # Dropping a course
    student2.drop_course("Physics")
    student2.drop_course("Biology")  # Attempt to drop a non-enrolled course

    # Displaying student details
    print(student1.get_student_info())
    print(student2.get_student_info())

    # Deleting a student
    del student1
    print(f"Currently active students: {Student.student_count}")

if __name__ == "__main__":
    manage_students()
```

---

## Key Features 🌟

- **Dynamic Student Management**:
  - Tracks total students dynamically.
  - Provides detailed student information.

- **Course Enrollment and Management**:
  - Handles enrollment and dropping of courses with validation.

- **Age Calculation**:
  - Automatically calculates a student's age based on their date of birth.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses Python’s standard library).

---

## Installation and Setup 🚀

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `04_student_enrollment.py`.
3. Run the script:

   ```bash
   python 04_student_enrollment.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Student Alice (ID: S001) enrolled on 2024-12-12. Total students: 1
Student Bob (ID: S002) enrolled on 2024-12-12. Total students: 2
Alice has been enrolled in Mathematics.
Alice has been enrolled in Computer Science.
Alice is already enrolled in Mathematics.
Bob has dropped Physics.
Bob is not enrolled in Biology.
{'student_id': 'S001', 'name': 'Alice', 'age': 22, 'enrollment_date': datetime.date(2024, 12, 12), 'courses': ['Mathematics', 'Computer Science']}
{'student_id': 'S002', 'name': 'Bob', 'age': 23, 'enrollment_date': datetime.date(2024, 12, 12), 'courses': ['Mathematics']}
Student Alice (ID: S001) record deleted. Total students: 1
Currently active students: 1
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

