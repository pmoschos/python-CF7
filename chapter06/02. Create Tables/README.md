# 🗂️ MySQL Connection and Table Creation Script 📝

This Python script demonstrates how to connect to a MySQL database server, select a specific database, and create tables programmatically using the `mysql-connector-python` library.

---

## Script Overview 📘

The script includes the following functionalities:

1. **Create Connection**:
   - Establishes a connection to the MySQL server using credentials (host, user, password, database, port).
2. **Create Tables**:
   - Dynamically creates tables in the selected database using SQL commands.
3. **Error Handling**:
   - Handles and logs potential errors during connection or table creation.

### :computer: Script Code

```python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, port):
    """
    Create a database connection to a MySQL server.
    
    Parameters:
    host_name (str): The name of the host.
    user_name (str): The user name used to authenticate.
    user_password (str): The password used to authenticate.
    db_name (str): The name of the database.
    port (str): The port number to connect to.

    Returns:
    conn: A MySQLConnection object or None if the connection failed.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
            port=port
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: '{e}' occurred")
    return connection

def create_tables(connection):
    """
    Create tables in the provided MySQL database connection.

    Parameters:
    connection: A MySQLConnection object.
    """
    create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        age INTEGER
    )
    """
    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    )
    """
    cursor = connection.cursor()
    try:
        cursor.execute('BEGIN')
        cursor.execute(create_teachers_table)
        cursor.execute(create_students_table)
        connection.commit()
        print("Tables created successfully")
    except Error as e:
        print(f"Error: '{e}' occurred")
        connection.rollback()
    finally:
        cursor.close()

def main():
    """
    Main function to connect to the database and create tables.
    """
    conn = create_connection('localhost', 'root', 'root', 'coding2025', '3306')
    if conn:
        create_tables(conn)
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Database Connection**: Establishes a secure connection to the MySQL server and selects a database.
- **Table Creation**: Dynamically creates tables using SQL commands.
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

3. Save the script as `create_tables.py`.
4. Update the script with appropriate MySQL credentials (`host_name`, `user_name`, `user_password`, `db_name`, `port`).
5. Run the script:

   ```bash
   python create_tables.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Connection to MySQL DB successful
Tables created successfully
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

