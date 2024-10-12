from menu.CitationUI import CitationUI
from menu.DriverUI import DriverUI
from menu.ParkingLotUI import ParkingLotUI
from menu.PermitUI import PermitUI
from menu.SpacesUI import SpacesUI
from menu.VehicleUI import VehicleUI
from menu.ZoneUI import ZoneUI
from connection.connection import connection

def main_menu():
    db = connection()
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
