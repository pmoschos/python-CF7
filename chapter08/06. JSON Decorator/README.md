# 📄 JSON Support Decorator Script 🔧

This Python script demonstrates the use of a decorator to add JSON serialization support to a class. The `add_json_support` decorator adds a `to_json` method to the target class, enabling easy conversion of its attributes to a JSON string.

---

## Script Overview 📘

### Function: `add_json_support`

1. **Purpose**:
   - Adds a `to_json` method to a class for JSON serialization.

2. **Key Features**:
   - Converts object attributes to a JSON string.
   - Handles serialization of non-standard types like `date` using `default=str` in `json.dumps`.

3. **Reusable Decorator**:
   - Can be applied to any class to enable JSON serialization.

### Example Class: `Product`

1. **Attributes**:
   - `name`: The name of the product.
   - `price`: The price of the product.

2. **Behavior**:
   - Uses the `add_json_support` decorator to enable JSON serialization of its attributes.

### :computer: Script Code

```python
import json
from datetime import date, timedelta
from typing import Any, Type

def add_json_support(cls: Type) -> Type:
    """
    Decorator to add JSON support to a class by adding a `to_json` method.
    
    Args:
        cls (Type): The class to be extended with JSON support.
        
    Returns:
        Type: The class with the added `to_json` method.
    """
    def to_json(self) -> str:
        """
        Convert the object's attributes to a JSON string.
        
        Returns:
            str: A JSON representation of the object's attributes.
        """
        return json.dumps(self.__dict__, default=str)
    
    cls.to_json = to_json
    return cls

@add_json_support
class Product:
    """
    A class representing a product with a name and price.
    
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

def main() -> None:
    """
    Main function to demonstrate JSON support for the Product class.
    """
    product = Product("Laptop", 1200)
    print(product.to_json())  # Output: {"name": "Laptop", "price": 1200}

    # Demonstrating support for additional types
    product_with_date = Product("Smartphone", 800)
    product_with_date.launch_date = date.today()
    print(product_with_date.to_json())  # Handles date serialization

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Dynamic JSON Serialization**:
  - Adds JSON serialization support to any class using a decorator.
  - Automatically handles standard and non-standard types like `date`.

- **Reusable Decorator**:
  - Easily applied to multiple classes for consistent behavior.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses Python’s standard library).

---

## Installation and Setup 🚀

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `06_json_decorator.py`.
3. Run the script:

   ```bash
   python 06_json_decorator.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
{"name": "Laptop", "price": 1200}
{"name": "Smartphone", "price": 800, "launch_date": "2024-12-12"}
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