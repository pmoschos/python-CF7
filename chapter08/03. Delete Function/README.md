# 🌐 Server Connection Management Script 🔌

This Python script demonstrates the management of server connections using a class-based approach. It tracks active connections and adjusts the count dynamically as connections are created and destroyed.

---

## Script Overview 📘

### Class Definition: `ServerConnection`

1. **Attributes**:
   - `connection_id`: A unique identifier for the connection instance.
   - `active_connections`: A class-level attribute tracking the number of active connections.

2. **Methods**:
   - `__init__`: Initializes a new connection, increments the active connections count, and logs the connection establishment.
   - `__del__`: Decrements the active connections count and logs the connection closure.

### :computer: Script Code

```python
class ServerConnection:
    """Class to represent and manage server connections."""
    active_connections = 0

    def __init__(self, connection_id):
        self.connection_id = connection_id
        ServerConnection.active_connections += 1
        print(f"Connection {self.connection_id} established. Active connections: {ServerConnection.active_connections}")

    def __del__(self):
        ServerConnection.active_connections -= 1
        print(f"Connection {self.connection_id} closed. Active connections: {ServerConnection.active_connections}")

# Example usage
def main():
    # Establish multiple connections
    conn1 = ServerConnection("001")
    conn2 = ServerConnection("002")
    conn3 = ServerConnection("003")

    # Check current active connections
    print(f"Currently active connections: {ServerConnection.active_connections}")

    # Close a connection
    del conn2
    print(f"Currently active connections after closing conn2: {ServerConnection.active_connections}")

    # Closing remaining connections
    del conn1
    del conn3
    print(f"Currently active connections after closing all connections: {ServerConnection.active_connections}")

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Dynamic Resource Management**:
  - Tracks the number of active server connections.
  - Adjusts counts automatically when connections are established or closed.

- **Logging**:
  - Logs messages to indicate when connections are created or destroyed.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses Python’s standard library).

---

## Installation and Setup 🚀

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `03_delete_function.py`.
3. Run the script:

   ```bash
   python 03_delete_function.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Connection 001 established. Active connections: 1
Connection 002 established. Active connections: 2
Connection 003 established. Active connections: 3
Currently active connections: 3
Connection 002 closed. Active connections: 2
Currently active connections after closing conn2: 2
Connection 001 closed. Active connections: 1
Connection 003 closed. Active connections: 0
Currently active connections after closing all connections: 0
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

