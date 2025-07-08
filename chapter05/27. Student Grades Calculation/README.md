# ✅ Average Grade Threshold Script 🎓

This Python script calculates the average grades of students and filters the results to display only those with averages exceeding a user-specified threshold. It is an interactive program with input validation and displays results clearly.

---

## Script Overview 📘

The script uses a dictionary to store student names and their respective grades. It prompts the user to enter a threshold value, validates the input, calculates average grades, and filters the students whose averages exceed the threshold. Results are presented in a user-friendly format.

### :computer: Script Code

```python
students = {
    'Alice': [85, 92, 78],
    'Bob': [79, 95, 88],
    'Charlie': [68, 72, 80],
    'Diana': [95, 98, 100],
    'Eve': [50, 60, 58]
}

def main():
    # Input validation loop
    while True:
        try:
            threshold = int(input("Please insert the threshold (integer): "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate average grades above the threshold
    average_grades = {
        student: round(sum(grades) / len(grades), 2)
        for student, grades in students.items()
        if grades and sum(grades) / len(grades) > threshold
    }

    # Display results
    if not average_grades:
        print(f"No students have an average grade greater than {threshold}.")
    else:
        print(f"\nStudents with average grade greater than {threshold}:")
        for student, avg_grade in average_grades.items():
            print(f"{student}: {avg_grade:.2f}")

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Input Validation**: Ensures the user provides a valid integer for the threshold.
- **Dynamic Average Calculation**: Automatically calculates average grades for students.
- **Filtered Output**: Displays results for students exceeding the specified threshold.
- **User-Friendly Interface**: Clear prompts and messages for a smooth user experience.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `27_student_grades.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `27_student_grades.py`.
5. Run the script with:

   ```bash
   python 27_student_grades.py
   ```

---

## Usage Example 📋

### Sample Input

```plaintext
Please insert the threshold (integer): 80
```

### Expected Output

```plaintext
Students with average grade greater than 80:
Alice: 85.00
Bob: 87.33
Diana: 97.67
```

If no students exceed the threshold:

```plaintext
No students have an average grade greater than 100.
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