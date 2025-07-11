# 🔧 MySQL Connection and Update Operation Script 🔄

This Python script demonstrates how to connect to a MySQL database server, select a specific database, and update records in a table using the `mysql-connector-python` library.

---

## Script Overview 📘

The script includes the following functionalities:

1. **Create Connection**:
   - Establishes a connection to the MySQL server using credentials (host, user, password, database, port).
2. **Update Data**:
   - Dynamically updates a record in the `teachers` table.
3. **Error Handling**:
   - Handles and logs potential errors during connection or data update.

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

def update_teacher(connection, teacher):
    """
    Update a teacher's information in the teachers table.

    Parameters:
    connection: A MySQLConnection object.
    teacher (tuple): A tuple containing the teacher's firstname, lastname, and age, and id.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE teachers SET firstname = %s, lastname = %s, age = %s WHERE id = %s",
            teacher
        )
        connection.commit()
        print("Teacher updated successfully")
    except Error as e:
        print(f"Error: '{e}' occurred")
        connection.rollback()
    finally:
        cursor.close()

def main():
    """
    Main function to connect to the database and update a teacher.
    """
    conn = create_connection('localhost', 'root', 'root', 'coding2025', '3306')
    if conn:
        teacher = ("Alice", "Smith", 45, 2)  # New values for firstname, lastname, and age, with id to identify the teacher
        update_teacher(conn, teacher)
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Database Connection**: Establishes a secure connection to the MySQL server and selects a database.
- **Data Update**: Dynamically updates records in the `teachers` table.
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

3. Save the script as `update_data.py`.
4. Update the script with appropriate MySQL credentials (`host_name`, `user_name`, `user_password`, `db_name`, `port`).
5. Run the script:

   ```bash
   python update_data.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Connection to MySQL DB successful
Teacher updated successfully
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

