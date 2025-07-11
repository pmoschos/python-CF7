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
