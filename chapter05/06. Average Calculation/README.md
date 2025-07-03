# 📊 Average Calculation Script ➗

Welcome to the Average Calculation Script! This script demonstrates how to calculate the average of a given set of numbers using variable-length arguments in Python.

## Key Features 🌟

- **Variable-Length Arguments**: Learn how to define and use functions with variable-length argument lists in Python.
- **Average Calculation**: Discover how to calculate the average of a set of numbers, handling cases where no arguments are provided.
- **Multiple Approaches**: Understand different approaches to implement the average calculation.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `average_calculation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `average_calculation.py`.
5. Run the script with: `python average_calculation.py`.

## Script Code 📘

```python
def avg(*args):
    """
    Calculate the average of the given numbers.

    Parameters:
    *args (float or int): A variable number of arguments which are the numbers to average.

    Returns:
    float: The average of the numbers. Returns 0 if no arguments are provided.
    """
    return sum(args) / len(args) if args else 0

def main():
    """
    Main function to demonstrate the usage of avg function.
    """
    # Define a list of integers
    my_ints = [10, 5, 9]
    
    # Calculate and print the average using the avg function
    print("Average of my_ints:", avg(*my_ints))  # Expected output: 8.0

    # Calculate and print the average of different sets of numbers
    print("Average of 1, 2, 3:", avg(1, 2, 3))  # Expected output: 2.0
    print("Average of 5, 10, 15:", avg(5, 10, 15))  # Expected output: 10.0
    print("Average of no numbers:", avg())  # Expected output: 0

if __name__ == "__main__":
    main()
```

## Usage Example 📋

Execute the script to see how the average calculation works using variable-length arguments. The script will demonstrate different sets of numbers, including an empty set, and display their averages.

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
