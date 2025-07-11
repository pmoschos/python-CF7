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
