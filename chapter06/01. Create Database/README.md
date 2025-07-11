# 🌐 MySQL Connection and Database Creation Script 🔄

This Python script demonstrates how to connect to a MySQL database server and create a database programmatically using the `mysql-connector-python` library.

---

## Script Overview 📘

The script includes the following functionalities:

1. **Create Connection**:
   - Establishes a connection to the MySQL server using credentials (host, user, password).
2. **Create Database**:
   - Executes an SQL query to create a new database on the connected server.
3. **Error Handling**:
   - Handles and logs potential errors during connection or database creation.

### :computer: Script Code

```python
import mysql.connector
from mysql.connector import Error

# pip install mysql-connector-python

def create_connection(host_name, user_name, user_password):
    """
    Create a database connection to a MySQL server.
    
    Parameters:
    host_name (str): The name of the host.
    user_name (str): The user name used to authenticate.
    user_password (str): The password used to authenticate.

    Returns:
    conn: A MySQLConnection object or None if the connection failed.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: '{e}' occurred")
    return connection

def create_database(connection, query):
    """
    Create a database using the provided connection and query.

    Parameters:
    connection: A MySQLConnection object.
    query (str): The SQL query to create a database.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"Error: '{e}' occurred")
    finally:
        cursor.close()

def main():
    """
    Main function to create a database.
    """
    conn = create_connection('localhost', 'root', 'root')
    if conn:
        create_database_query = "CREATE DATABASE coding2025"
        create_database(conn, create_database_query)
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Database Connection**: Establishes a secure connection to the MySQL server.
- **Database Creation**: Dynamically creates a new database using SQL commands.
- **Error Handling**: Catches and reports errors during database connection and query execution.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Library**: `mysql-connector-python` (Install using `pip install mysql-connector-python`).
- **MySQL Server**: A running MySQL server is required.

---

## Installation and Setup 🚀

1. Ensure Python 3.x and MySQL server are installed on your machine.
2. Install the required library:

   ```bash
   pip install mysql-connector-python
   ```

3. Save the script as `create_db.py`.
4. Update the script with appropriate MySQL credentials (`host_name`, `user_name`, `user_password`).
5. Run the script:

   ```bash
   python create_db.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Connection to MySQL DB successful
Database created successfully
MySQL connection is closed
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