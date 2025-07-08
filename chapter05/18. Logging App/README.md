# 📜 Logging in Python with File Handlers 🔧

This script demonstrates how to implement logging in Python using file handlers. It redirects error messages from the console to a log file, providing a practical approach to handling errors in a production environment.

## Script Overview 📘

The script sets up a logger to write error messages to a log file. It attempts to find a specific number in a list and logs an error if the number is not found. This example highlights how to use the `logging` module to capture and store error information.

### :computer: Script Code

```python
import logging
from typing import List, Any

def configure_logger(log_file: str, logger_name: str) -> logging.Logger:
    """
    Configure and return a logger with both file and console handlers.

    Args:
        log_file (str): The name of the log file.
        logger_name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)  # Set the logging level

    # Level      | Severity   | Description
    # ---------- | ---------- | ----------------------------------------------------------
    # DEBUG      | Lowest     | Detailed diagnostic information for debugging.
    # INFO       | Low        | Informational messages that confirm normal operation.
    # WARNING    | Medium     | Potential issues that might require attention.
    # ERROR      | High       | Errors that prevent part of the program from functioning.
    # CRITICAL   | Highest    | Serious errors causing application-wide issues or crashes.

    # File handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    )

    # Mode       | Purpose          | Description
    # ---------- | ---------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 'a'        | Append           | Opens the file for appending. Logs are added at the end of the file without overwriting existing content. Creates the file if it doesn’t exist.
    # 'w'        | Write            | Opens the file for writing. Overwrites the file if it exists; creates a new file if it doesn’t.
    # 'x'        | Exclusive Create | Creates a new file for writing. Raises an error if the file already exists.
    # 'r'        | Read             | Opens the file for reading only. Raises an error if the file doesn’t exist.
    # 'r+'       | Read/Write       | Opens the file for both reading and writing. The file pointer is at the beginning. Raises an error if the file doesn’t exist.
    # 'a+'       | Append/Read      | Opens the file for appending and reading. The file pointer is at the end for writing, but you can read the content as well. Creates the file if it doesn’t exist.
    # 'w+'       | Write/Read       | Opens the file for both writing and reading. Overwrites the file if it exists; creates a new file if it doesn’t.
    # 'x+'       | Create/Read/Write| Creates a new file for both reading and writing. Raises an error if the file already exists.
    # 'b'        | Binary Mode      | Opens the file in binary mode. Commonly used with other modes like 'rb', 'wb', or 'ab' for binary read/write/append.
    # 't'        | Text Mode        | Opens the file in text mode. This is the default mode and often used implicitly.

    # Console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    )

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def search_item(items: List[Any], item_to_find: Any, logger: logging.Logger) -> int:
    """
    Search for an item in a list and return its index.

    Args:
        items (List[Any]): List of items to search within.
        item_to_find (Any): The item to find.
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        int: The index of the item in the list.

    Raises:
        ValueError: If the item is not found.
    """
    if not items:
        logger.warning("The list is empty.")
        raise ValueError("Cannot search in an empty list.")
    
    try:
        index = items.index(item_to_find)
        logger.info(f"Item '{item_to_find}' found at index {index}.")
        return index
    except ValueError as e:
        logger.error(f"Item '{item_to_find}' not found in the list. Error: {e}", exc_info=True)
        raise  # Re-raise the same ValueError

def main():
    # Log file name
    log_file = 'cf6.log'

    # Configure logger
    logger = configure_logger(log_file, 'search-app')

        # List of employee names to search within
    employee_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    # Employee name to search for in the list
    employee_to_find = "Frank"

    try:
        # Attempt to find the index of employee_to_find in employee_names
        index = search_item(employee_names, employee_to_find, logger)
        print(f"Employee '{employee_to_find}' found at index {index}.")
    except ValueError:
        print(f"Employee '{employee_to_find}' was not found in the list.")


if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Logging**: Learn how to implement logging in Python using the `logging` module.
- **File Handlers**: Understand how to use file handlers to redirect log messages to a file.
- **Error Handling**: See how to log errors when they occur, capturing valuable debug information.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in `logging` module

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `18_logging_app.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `18_logging_app.py`.
5. Run the script with: `python 18_logging_app.py`.

## Usage Example 📋
Execute the script to see how logging is implemented. The script will attempt to find a number in a list and log an error if the number is not found. Check the generated `cf5.log` file to view the logged error messages.

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
