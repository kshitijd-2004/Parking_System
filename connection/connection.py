import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self):
        self.connection = None

    def connect(self):
        """ Connect to MySQL database """
        try:
            self.connection = mysql.connector.connect(
                host='Host',
                port=0,
                database='parking_system',
                user='user_name',
                password='password'
            )
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print(f"Connected to MySQL Server version {db_info}")
                cursor = self.connection.cursor()
                cursor.execute("SELECT DATABASE();")
                record = cursor.fetchone()
                print(f"You're connected to database: {record[0]}")
                return self.connection

        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

        # Removed the finally block since we want to keep the connection open
        # and return the connection object.


# Test the connection
if __name__ == '__main__':
    db_connection = Connection()
    connection = db_connection.connect()

    if connection is not None and connection.is_connected():
        print("Connection established successfully!")
    else:
        print("Failed to establish connection.")
