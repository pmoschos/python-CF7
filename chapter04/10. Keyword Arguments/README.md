# ✅ Python Keyword Arguments Filtering Script ✂️

Welcome to the Python Keyword Arguments Filtering Script! This script demonstrates how to filter a list of products based on given criteria using keyword arguments.

## Script Overview 📘

The script defines a function `get_results` that filters a list of products based on the provided keyword arguments. Each keyword argument corresponds to a product attribute such as brand and price.

### :computer: Script Code

```python
from typing import List, Tuple, Dict, Optional

def get_results(products: List[Tuple[str, int]], **kwargs: Optional[Dict[str, str | int]]) -> List[Tuple[str, int]]:
    """
    Filters a list of products based on given keyword arguments.
    Each keyword argument corresponds to a product attribute.

    Parameters:
        products (List[Tuple[str, int]]): A list of tuples where each tuple contains a brand and a price.
        **kwargs (Dict[str, str | int]): Arbitrary keyword arguments for filtering (e.g., brand, price).

    Example:
    >>> products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    >>> get_results(products, brand="lenovo", price=100)
    [('lenovo', 100)]
    """
    # Improved filtering to allow matching on one or more provided criteria
    results = [
        # [<expression> for <item> in <iterable> if <condition>]
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results

def main():
    """
    Main function to demonstrate the use of get_results function.
    """
    products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    # Demonstration of the function
    print(get_results(products, **criteria))

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Keyword Arguments Filtering**: Learn how to filter a list of items using keyword arguments.
- **Dynamic Filtering**: Discover how to dynamically match items based on one or more provided criteria.
- **List Comprehension**: Understand how to use list comprehensions for concise and readable code.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `10_keyword_arguments.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `10_keyword_arguments.py`.
5. Run the script with: `python 10_keyword_arguments.py`.

## Usage Example 📋

Execute the script to see how keyword arguments can be used to filter a list of products. The script will demonstrate filtering the products list based on the given criteria and display the matching results.

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