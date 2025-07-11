# 🗂️ JSON Serialization and Object Representation in Python 💾

This script demonstrates the creation of a JSON serialization decorator, `add_json_support`, which enables Python classes to easily serialize their attributes into JSON format. The script highlights handling of non-serializable types like `date` and `timedelta` while offering practical examples with `Product` and `Student` classes.

## Script Overview 📘

### Features
- **Decorator Implementation**: Adds a reusable JSON serialization capability to any Python class.
- **Serialization Support**: Handles types like `date` and `timedelta` for JSON output.
- **Examples**: Demonstrates the functionality with `Product` and `Student` classes.
- **Edge Case Handling**: Demonstrates error handling for unsupported serialization types.

### Script Code

```python
import json
from datetime import date, timedelta
from typing import Type, Any, List

def add_json_support(cls: Type) -> Type:
    """
    Decorator to add JSON support with handling for non-serializable types.
    Adds a `to_json` method to the decorated class.
    
    Args:
        cls (Type): The class to be decorated.

    Returns:
        Type: The decorated class with `to_json` support.
    """
    def to_json(self) -> str:
        """
        Converts the object's attributes to a JSON string, handling custom types.
        
        Returns:
            str: JSON representation of the object.
        """
        def custom_serializer(obj: Any) -> Any:
            if isinstance(obj, (date, timedelta)):
                return obj.isoformat()  # Convert to ISO 8601 string
            raise TypeError(f"Type {type(obj)} not serializable")

        return json.dumps(self.__dict__, default=custom_serializer)
    
    cls.to_json = to_json
    return cls

@add_json_support
class Product:
    """
    A class representing a product with a name and price.
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

@add_json_support
class Student:
    """
    A class representing a student with an ID, name, and date of birth.
    """
    def __init__(self, student_id: str, name: str, date_of_birth: date, courses: List[str] = None) -> None:
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.courses = courses if courses else []  # List of enrolled courses
        self.enrollment_date = date.today()

def main() -> None:
    """
    Main function to demonstrate JSON serialization for Product and Student classes.
    """
    product = Product("Laptop", 1200)
    print("Product JSON:", product.to_json())

    student1 = Student("S001", "Alice", date(2002, 5, 15))
    student2 = Student("S002", "Bob", date(2001, 8, 22), ["Mathematics", "Physics"])
    
    print("Student 1 JSON:", student1.to_json())
    print("Student 2 JSON:", student2.to_json())

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Custom Serialization**: Enables JSON serialization of attributes, including handling of special types like `date` and `timedelta`.
- **Decorator Pattern**: Encapsulates functionality to add features to classes dynamically.
- **Edge Case Management**: Provides robust error handling for unsupported types.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses built-in `json` and `datetime` modules).

## Installation and Setup 🚀
1. Ensure Python 3.x is installed on your system.
2. Save the script as `07_extended_json_example.py`.
3. Run the script in a terminal or an IDE with the command:
   ```bash
   python 07_extended_json_example.py
   ```

## Usage Example 📋
Execute the script to:
- Serialize a `Product` object into JSON.
- Serialize multiple `Student` objects into JSON, demonstrating handling of dates and lists.
- View error handling for unsupported types.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 🔄 License
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

