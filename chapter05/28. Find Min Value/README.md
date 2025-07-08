# 🔍 Find Minimum Value Key Script 🔑

This Python script demonstrates how to find specific keys in a dictionary based on certain criteria. The example provided identifies the student with the lowest grade, the alphabetically smallest name, and the shortest name by length.

---

## Script Overview 📘

The script processes a dictionary of students and their grades. It includes logic to handle empty dictionaries and demonstrates three specific operations:

1. **Lowest Grade**: Finds the key (student) with the minimum value (grade).
2. **Alphabetically Smallest Name**: Finds the key that is the smallest alphabetically.
3. **Shortest Name**: Finds the key with the shortest length.

### :computer: Script Code

```python
def main():
    """
    Main function to demonstrate finding the key with the minimum value in a dictionary.
    This example finds the student with the lowest grade, the alphabetically smallest name,
    and the shortest name by length.
    """
    # Define a dictionary with students and their corresponding grades
    student_grades = {
        'Alice': 85,
        'Bob': 72,
        'Charlie': 90,
        'David': 68
    }

    # Handle edge case: empty dictionary
    if not student_grades:
        print("No student data available.")
        return

    # Find the student with the lowest grade
    student_with_lowest_grade = min(student_grades, key=student_grades.get)
    print(f"Student with the lowest grade: {student_with_lowest_grade} (Grade: {student_grades[student_with_lowest_grade]})")

    # Find the student with the smallest name alphabetically
    student_with_smallest_name = min(student_grades)
    print(f"Student with the smallest name (alphabetically): {student_with_smallest_name}")

    # Find the student with the shortest name by length
    student_with_shortest_name = min(student_grades, key=len)
    print(f"Student with the shortest name: {student_with_shortest_name} (Length: {len(student_with_shortest_name)})")

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Edge Case Handling**: Includes checks for empty dictionaries to avoid errors.
- **Custom Criteria**: Demonstrates finding keys based on both values and key properties.
- **Readable Output**: Provides clear and descriptive results for each operation.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `08_find_min_value.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `08_find_min_value.py`.
5. Run the script with:

   ```bash
   python find_min_value_key.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Student with the lowest grade: David (Grade: 68)
Student with the smallest name (alphabetically): Alice
Student with the shortest name: Bob (Length: 3)
```

If the dictionary is empty:

```plaintext
No student data available.
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

