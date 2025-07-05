# ✂️ Transforming and Filtering a List of Grades 🎓

This script demonstrates how to use list comprehensions and `map`/`filter` functions to transform and filter a list of grades in Python.

## Script Overview 📘

The script defines a `main` function that performs the following operations on a list of grades:
1. **Transformation**: Increase each grade by 1 if it's less than or equal to 9.
2. **Filtering**: Select grades that are greater than or equal to 5.

Both operations are demonstrated using list comprehensions and the `map`/`filter` functions.

### :computer: Script Code

```python
def main():
    """
    Main function to demonstrate the usage of list comprehensions and map/filter functions 
    to transform and filter a list of grades.
    """
    grades = [7, 5, 9, 10, 3]

    # Map (Transforms the data of the list) using list comprehension
    upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
    print("Final grades (list comprehension):", upscaled_grades)

    # Map (Transforms the data of the list) using map() function
    upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
    print("Final grades (map()):", upscaled_grades2)

    # Filter using list comprehension
    passed_grades = [grade for grade in grades if grade >= 5]
    print("Passed (list comprehension):", passed_grades)

    # Filter (Based on a predicate) using filter() function
    passed_grades2 = list(filter(lambda grade: grade >= 5, grades))
    print("Passed (filter()):", passed_grades2)

    # Show that filter returns an iterator
    print("Filter object:", filter(lambda grade: grade >= 5, grades))

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **List Comprehension**: Learn how to use list comprehensions to transform and filter data efficiently.
- **Map and Filter Functions**: Discover how to use the map and filter functions for data transformation and filtering.
- **Lambda Functions**: Understand how to use lambda functions for concise and readable code.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `11_transform_filter_grades.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `11_transform_filter_grades.py`.
5. Run the script with: `python 11_transform_filter_grades.py`.

## Usage Example 📋
Execute the script to see how grades are transformed and filtered using both list comprehensions and the map/filter functions. The script will demonstrate each method and print the results.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
