# 🌀 Set Operations in Python 🔀

This script demonstrates various set operations in Python, including intersection, union, difference, and symmetric difference. These operations are useful for comparing and manipulating sets of data.

## Script Overview 📘

The script defines two sets and performs several operations to find common elements, all elements, elements in one set but not the other, and elements in either set but not both.

### :computer: Script Code

```python
def main():
    """
    Demonstrates set operations.
    """
    # Define two sets of products available in two different stores
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Watermelons"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

    # Find common products (intersection) available in both stores
    common_products = store_a_products & store_b_products
    print("Products available in both Store A and Store B:", common_products)
    # Alternatively, using the intersection method
    common_products = store_a_products.intersection(store_b_products)
    print("Products available in both Store A and Store B:", common_products)

    # Find all unique products (union) across both stores
    all_products = store_a_products | store_b_products
    print("All unique products across Store A and Store B:", all_products)
    # Alternatively, using the union method
    all_products = store_a_products.union(store_b_products)
    print("All unique products across Store A and Store B:", all_products)

    # Find products available in Store A but not in Store B (difference)
    store_a_exclusive = store_a_products - store_b_products
    print("Products available only in Store A:", store_a_exclusive)
    # Alternatively, using the difference method
    store_a_exclusive = store_a_products.difference(store_b_products)
    print("Products available only in Store A:", store_a_exclusive)

    # Find products available in Store B but not in Store A (difference)
    store_b_exclusive = store_b_products - store_a_products
    print("Products available only in Store B:", store_b_exclusive)
    # Alternatively, using the difference method
    store_b_exclusive = store_b_products.difference(store_a_products)
    print("Products available only in Store B:", store_b_exclusive)

    # Find products that are in either Store A or Store B but not in both (symmetric difference)
    unique_to_either_store = store_a_products ^ store_b_products
    print("Products available in either Store A or Store B but not both:", unique_to_either_store)
    # Alternatively, using the symmetric_difference method
    unique_to_either_store = store_a_products.symmetric_difference(store_b_products)
    print("Products available in either Store A or Store B but not both:", unique_to_either_store)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Set Operations**: Learn how to perform various set operations such as intersection, union, difference, and symmetric difference.
- **Methods**: Understand the use of set methods like `intersection`, `union`, `difference`, and `symmetric_difference`.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in set operations

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `20_set_operations.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `20_set_operations.py`.
5. Run the script with: `python 20_set_operations.py`.

## Usage Example 📋
Execute the script to see how set operations are performed. The script will output the common elements, all elements, elements in one set but not the other, and elements in either set but not both.

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
