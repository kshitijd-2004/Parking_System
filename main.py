import mysql.connector
from mysql.connector import Error
from menu.CitationUI import CitationUI
from menu.DriverUI import DriverUI
from menu.ParkingLotUI import ParkingLotUI
from menu.PermitUI import PermitUI
from menu.SpacesUI import SpacesUI
from menu.VehicleUI import VehicleUI
from menu.ZoneUI import ZoneUI



class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """ Connect to MySQL database """
        try:
            self.connection = mysql.connector.connect(
                host='127.0.0.1',
                port=3307,
                database='parking_system',
                user='dhande',
                password='Siya2008'
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

def main_menu():
    db = DatabaseConnection()
    db.initialize()
    while True:
        print("ParkingSystem DB")
        print("Menu:")
        print("1. Driver")
        print("2. Vehicle")
        print("3. Citation")
        print("4. ParkingLot")
        print("5. Permit")
        print("6. Zones")
        print("7. Spaces")
        print("8. EXIT")

        choice = input("Enter your Choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                DriverUI.driverUI(db.connection)
            elif choice == 2:
                VehicleUI.vehicleUI(db.connection)
            elif choice == 3:
                CitationUI.citationUI(db.connection)
            elif choice == 4:
                ParkingLotUI.parkinglotUI(db.connection)
            elif choice == 5:
                PermitUI.permitUI(db.connection)
            elif choice == 6:
                ZoneUI.zoneUI(db.connection)
            elif choice == 7:
                SpacesUI.spacesUI(db.connection)
            elif choice == 8:
                break
            else:
                print("Please enter a valid choice")
        except ValueError:
            print("Please enter a valid integer choice")

    db.close_connection()
    print("Connection closed")

if __name__ == '__main__':
    main_menu()
