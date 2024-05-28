from crud import ParkingLotCRUD

class ParkingLotUI:
    def __int__(self, connection):
        self.crud = ParkingLotCRUD(connection)

    def parkinglotUI(self):
        while True:
            print("1. Enter Parking Lot Information")
            print("2. Update Parking Lot Information")
            print("3. Delete Parking Lot Information")
            print("4. View Parking Lot Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice")
            if not choice.isdigit():
                print("Enter a choice from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated Lot Name and Address: ").split('|')
                if len(data) != 2:
                    print("Invalid input, please enter all required fields")
                    continue

                lot_name, address = data

                if self.crud.addParkingLot(lot_name, address):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 2:
                data = input("Enter | separated Lot Name and Address: ").split('|')
                if len(data) != 2:
                    print("Invalid input, please enter all required fields")
                    continue

                lot_name, address = data

                if self.crud.updateParkingLot(lot_name, address):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 3:
                lot_name = input("Enter Lot Name: ")
                if self.crud.removeParkingLot(lot_name):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 4:
                parking_lots = self.crud.viewParkingLots()

                if not parking_lots:
                    print("No parking lots to display")
                    continue
                print("| ParkingLot | Address |")
                print("|------------|---------|")
                for parking_lot in parking_lots:
                    print(f'| {parking_lot.lot_name:<10} | {parking_lot.address}:<7')

            elif choice == 5:
                break

            else:
                print("Enter a valid choice from 1 to 5")