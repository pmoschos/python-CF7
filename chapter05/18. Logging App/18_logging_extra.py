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
