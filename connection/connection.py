import mysql.connector
from mysql.connector import Error

class connection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """ Connect to MySQL database """
        try:
            self.connection = mysql.connector.connect(
                host='host',
                port=3307,
                database='parking_system',
                user='user',
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

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection closed")

    def initialize(self):
        self.connect()