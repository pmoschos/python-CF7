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
