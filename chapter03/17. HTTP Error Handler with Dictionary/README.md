# 🌐 Python HTTP Error Code Handler ❌

Welcome to the Python HTTP Error Code Handler script! This script returns the HTTP error message corresponding to a given error code using a dictionary. It's an ideal resource for understanding dictionary usage and conditional statements in Python.

## Script Overview 📘

The script defines a function to map HTTP error codes to their corresponding messages using a dictionary and demonstrates its usage with an example error code.

### :computer: Script Code

```python
def get_http_error(error_code):
    """
    Returns the HTTP error message corresponding to the given error code.
    
    Args:
    error_code (int): The HTTP error code.
    
    Returns:
    str: The corresponding error message.
    """
    
    error_messages = {
        200: "OK",
        400: "Bad request",
        404: "Not found"
    }
    return error_messages.get(error_code, "Unknown error")

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Dictionary Usage**: Learn how to use dictionaries to map error codes to their corresponding messages.
- **HTTP Error Codes**: Discover how to handle various HTTP error codes and their messages.
- **Function Definition**: Understand how to define and use functions in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x or higher is installed on your machine.
2. Save the script as `17_http_error_handler_with_dict.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `17_http_error_handler_with_dict.py`.
5. Run the script with: `python 17_http_error_handler_with_dict.py`.

## Usage Example 📋

Execute the script to see the HTTP error message corresponding to the given error code printed in the console.

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