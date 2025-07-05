# 🌡️ Fahrenheit to Celsius Conversion 🔄

This script demonstrates how to convert temperatures from Fahrenheit to Celsius using both list comprehensions and generator expressions in Python.

## Script Overview 📘

The script defines a `main` function that performs the conversion of a list of Fahrenheit temperatures to Celsius using two different approaches: list comprehension and generator expressions. It also demonstrates how to print the results.

### :computer: Script Code

```python
def main():
    """
    Main function to demonstrate the conversion of Fahrenheit to Celsius using both
    list comprehension and generator expression.
    """
    fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]

    # Generate a list of Celsius temperatures using list comprehension
    celcius_temps_list = ["{:.2f}".format((temp - 32) * 5 / 9) for temp in fahrenheit_temps]
    print("Celsius temperatures (list comprehension):", celcius_temps_list)

    # Generate a generator for Celsius temperatures
    celcius_temps_gen = ("{:.2f}".format((temp - 32) * 5 / 9) for temp in fahrenheit_temps)
    print("Celsius temperatures (generator expression):", celcius_temps_gen)

    # Print each Celsius temperature from the generator
    for celcius in celcius_temps_gen:
        print(celcius)

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **List Comprehension**: Learn how to use list comprehensions for concise and efficient temperature conversion.
- **Generator Expressions**: Discover how to use generator expressions to create memory-efficient temperature conversions.
- **Formatted Output**: Understand how to format numerical output to two decimal places for better readability.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `10_temperature_converter.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `10_temperature_converter.py`.
5. Run the script with: `python 10_temperature_converter.py`.

## Usage Example 📋
Execute the script to see how temperatures in Fahrenheit are converted to Celsius using both list comprehensions and generator expressions. The script will demonstrate both methods and print the results.

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
