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
