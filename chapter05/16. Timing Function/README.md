# 🕒 Timing Function Execution ⏱️

This script demonstrates how to measure the execution time of a function in Python using the `time` module. The example function calculates the sum of numbers from 0 to `n-1` and prints the time taken for the calculation.

## Script Overview 📘

The script defines a `get_time` function that calculates the sum of numbers from 0 to `n-1` and measures the time taken for the computation. It then prints the elapsed time. The `main` function calls `get_time` with a sample input and prints the result.

### :computer: Script Code

```python
import time

def get_time(n):
    """
    Calculate the sum of the first n natural numbers and measure the time taken to perform the calculation.

    Parameters:
    n (int): The number of natural numbers to sum.

    Returns:
    int: The sum of the first n natural numbers.
    """
    start_time = time.time()  # Record the start time
    # Perform the calculation: sum of the first n natural numbers
    result = sum(range(n))  # 0 + 1 + 2 + 3 + ... + (n - 1)
    end_time = time.time()  # Record the end time
    # Print the time taken to run the function
    print(f"My function took {end_time - start_time: .5f} seconds to run")
    
    return result

def main():
    """
    Main function to demonstrate the get_time function.
    """
    # Call the get_time function with n = 1,000,000 and print the result
    print(get_time(1000000))

if __name__ == "__main__":
    main()
```


## Key Features 🌟
- **Time Measurement**: Learn how to measure the execution time of a function using the time module.
- **Performance Testing**: Understand how to use time measurements for performance testing of functions.
- **Formatted Output**: See how to format numerical output for readability.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `16_timing_function_execution.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `16_timing_function_execution.py`.
5. Run the script with: `python 16_timing_function_execution.py`.

## Usage Example 📋
Execute the script to see how the time taken for a function to execute is measured and printed. The script will demonstrate the timing of the calculation of the sum of numbers from 0 to `n-1`.

📢 Stay Updated
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