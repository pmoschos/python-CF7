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

def fetch_teachers(connection):
    """
    Fetch teachers from the teachers table.

    Parameters:
    connection: A MySQLConnection object.

    Returns:
    list: A list of tuples containing the fetched records.
    """
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, firstname, lastname FROM teachers")
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: '{e}' occurred")
        return []
    finally:
        cursor.close()

def main():
    """
    Main function to connect to the database and fetch teachers.
    """
    conn = create_connection('localhost', 'root', 'root', 'coding2025', '3306')
    if conn:
        results = fetch_teachers(conn)
        print(results)
        print(type(results))
        print()

        for result in results:
            print(f"ID: {result[0]}, Firstname: {result[1]}, Lastname: {result[2]}")
        
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
