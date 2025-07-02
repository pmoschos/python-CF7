# ✨ Filtering and Capitalizing City Names Script 🔄

Welcome to the Filtering and Capitalizing City Names Script! This script demonstrates how to filter city names based on their length and capitalize the filtered names using `filter`, `map`, and lambda functions.

## Script Overview 📘

The script defines a list of city names and uses a lambda function with the `filter` function to filter out city names longer than 5 characters. It then capitalizes these filtered names using another lambda function with the `map` function.

### :computer: Script Code

```python
# List of city names
cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

# Filtering city names longer than 5 characters using filter and lambda
long_cities = filter(lambda city: len(city) > 5, cities)

# Capitalizing the filtered city names using map and lambda
cap_length_cities = list(map(lambda city: city.title(), long_cities))

# All in one
# Filter and capitalize cities with more than 5 characters
cap_length_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

# Print the transformed list
print("Capitalized Cities with more than 5 characters:", cap_length_cities)

# For reference: Using list comprehension to achieve the same functionality
cap_length_cities_comprehension = [city.title() for city in cities if len(city) > 5]
print("Using list comprehension:", cap_length_cities_comprehension)
```

## Key Features 🌟

- **Filter Function**: Learn how to use the `filter` function to select elements from a list based on a condition.
- **Map Function**: Discover how to use the `map` function to apply a transformation to each element in a filtered list.
- **Lambda Function**: Understand how to define and use lambda functions for concise and readable code.
- **List Comprehension**: See an alternative approach using list comprehension to achieve the same result.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `16_map_filter_lambda.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `16_map_filter_lambda.py`.
5. Run the script with: `python 16_map_filter_lambda.py`.

## Usage Example 📋

Execute the script to see how to filter city names longer than 5 characters and capitalize them using the `filter` and `map` functions along with lambda functions. The script will demonstrate the transformation by printing the list of filtered and capitalized city names.

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
