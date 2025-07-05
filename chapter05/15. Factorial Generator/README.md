# ✨ Factorial Generator Script 🔄

This script demonstrates how to use a generator function to yield factorials indefinitely. The script uses a generator to calculate and print the factorials of numbers sequentially.

## Script Overview 📘

The script defines a `facto` generator function that yields factorials indefinitely. The `main` function creates a generator object and prints the first few factorials in sequence.

### :computer: Script Code

```python
def facto():
    """
    Generator function to yield factorials indefinitely.
    
    Yields:
    int: The next factorial in the sequence.
    """
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

def main():
    # Create a generator object for factorials
    f = facto()

    # Print the first 6 factorials (from 0! to 5!)
    for i in range(6):
        print(f"{i}! = {next(f)}")

    # Print the next 5 factorials (from 6! to 10!)
    for i in range(6, 11):
        print(f"{i}! = {next(f)}")

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Yield Statement**: Learn how to use the yield statement to create a generator that produces an infinite sequence of factorials.
- **Generator Function**: Understand how to implement a generator function that maintains state between successive calls to yield.
- **Indefinite Generation**: See how to create a generator that can produce an indefinite number of results.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `15_factorial_generator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `15_factorial_generator.py`.
5. Run the script with: `python 15_factorial_generator.py`.

## Usage Example 📋
Execute the script to see how the generator function yields factorials sequentially. The script will demonstrate the calculation of the first 11 factorials.

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
