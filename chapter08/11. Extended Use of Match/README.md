# ✉️ Message Handler Simulation Using 'match' Statement 🤝

Welcome to the Message Handler Simulation Script! This Python script demonstrates how to use the `match` statement introduced in Python 3.10 for pattern matching. The program processes various types of messages, showcasing the flexibility and expressiveness of the `match` statement.

## Script Overview 📘

The script includes:
- A `handle_message` function that uses `match` to process messages of different types, including strings, lists, dictionaries, and tuples.
- A main block that tests various scenarios to illustrate how the `match` statement works in Python.

### :computer: Script Code

```python
# A program that simulates a message handler using the 'match' statement.

def handle_message(message):
    """
    Handles various types of messages using the 'match' statement.

    Args:
        message: The message to handle, which can be of various types such as string, list, dictionary, or tuple.
    """
    match message:
        # Case for a simple greeting message "hello"
        case "hello":
            print("Hello there! How can I help you today?")
        
        # Case for a goodbye message "bye"
        case "bye":
            print("Goodbye! Have a nice day!")
        
        # Case for a list containing "weather" and a location
        case ["weather", location]:
            print(f"Checking the weather for {location}...")
        
        # Case for a dictionary with a "greet" command and a name
        case {"command": "greet", "name": name}:
            print(f"Hello, {name}! Nice to meet you.")
        
        # Case for a dictionary with a "sum" command and exactly two numbers
        case {"command": "sum", "numbers": [a, b]}:
            print(f"The sum of {a} and {b} is {a + b}.")
        
        # Case for a dictionary with a "sum" command and a list of numbers
        case {"command": "sum", "numbers": numbers}:
            total = sum(numbers)
            print(f"The total sum is {total}.")
        
        # Case for a tuple where both values are identical
        case (x, y) if x == y:
            print(f"The values are identical: x = {x}, y = {y}")
        
        # Case for a tuple where values are different
        case (x, y):
            print(f"The values are different: x = {x}, y = {y}")
        
        # Default case for unrecognized message formats
        case _:
            print("Unrecognized message format.")


# Test various cases to help students understand how pattern matching works.
if __name__ == "__main__":
    # Simple literal matching
    handle_message("hello")  # Should print a greeting message
    handle_message("bye")    # Should print a goodbye message

    # List matching
    handle_message(["weather", "Athens"])  # Should print a weather check message for Athens

    # Dictionary matching
    handle_message({"command": "greet", "name": "Panagiotis"})  # Should greet Panagiotis
    handle_message({"command": "sum", "numbers": [5, 3]})        # Should print the sum of 5 and 3
    handle_message({"command": "sum", "numbers": [1, 2, 3, 4]})  # Should print the total sum of 1, 2, 3, and 4

    # Tuple matching and additional conditions
    handle_message((5, 5))  # Should indicate that the values are identical
    handle_message((7, 3))  # Should indicate that the values are different

    # Unrecognized pattern
    handle_message("unknown")  # Should indicate that the message format is unrecognized
```

## Key Features 🌟

- **Pattern Matching**: Demonstrates how to use Python's `match` statement for various patterns.
- **Dynamic Message Handling**: Processes messages of different types, including strings, lists, dictionaries, and tuples.
- **Default Handling**: Provides a default case for unrecognized messages.

## Technical Requirements 🔧

- **Python Version**: Python 3.10 or later (required for the `match` statement).
- **External Libraries**: None (uses built-in Python functionalities).

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.10 or later is installed on your machine.
2. Save the script as `11_extended_match.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `11_extended_match.py`.
5. Run the script with: `python 11_extended_match.py`.

## Usage Example 📋

Execute the script to see how the `match` statement handles various message patterns:

1. **Greeting Example:**
    ```python
    handle_message("hello")
    # Output: Hello there! How can I help you today?
    ```

2. **Weather Example:**
    ```python
    handle_message(["weather", "Athens"])
    # Output: Checking the weather for Athens...
    ```

3. **Sum Command Example:**
    ```python
    handle_message({"command": "sum", "numbers": [5, 3]})
    # Output: The sum of 5 and 3 is 8.
    ```

4. **Default Case Example:**
    ```python
    handle_message("unknown")
    # Output: Unrecognized message format.
    ```

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

