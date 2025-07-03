# 📝 Event Logging Script 📄

This script demonstrates how to log events with a specified type and additional keyword arguments. Each event is timestamped and can include various attributes provided as keyword arguments.

## Script Overview 📘

The script defines a `log_event` function that logs an event with a specified type and additional keyword arguments. Each event includes a timestamp and any additional information passed to the function.

### :computer: Script Code

```python
from datetime import datetime

def log_event(event_type: str, **kwargs: dict) -> None:
    """
    Logs an event with a specified type and additional keyword arguments.

    Parameters:
    event_type (str): The type of event being logged.
    kwargs (dict): Additional information about the event.
    """
    timestamp = datetime.now().isoformat()
    print(f"Event type: {event_type}")
    print(f"Timestamp: {timestamp}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("-" * 40)  # Separator for readability

def main() -> None:
    """
    Main function for testing the log_event function.
    """
    # Example usage of the log_event function
    log_event("UserLogin", user="JohnDoe", status="Success", ip="192.168.1.1")
    log_event("FileUpload", user="JaneDoe", status="Failure", filename="report.pdf", reason="File too large")

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Event Logging**: Learn how to log events with a specified type and additional keyword arguments.
- **Timestamp Generation**: Discover how to generate and include timestamps in event logs.
- **Keyword Arguments**: Understand how to use keyword arguments to pass additional information to a function.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses the built-in datetime module)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `08_event_logger.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `08_event_logger.py`.
5. Run the script with: `python 08_event_logger.py`.

## Usage Example 📋
Execute the script to see how events are logged with timestamps and additional information. The script will demonstrate logging different types of events with various attributes.

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
