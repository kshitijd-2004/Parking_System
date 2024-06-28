from crud.DriverCRUD import DriverCRUD

class DriverUI:
    def __init__(self, connection):
        self.crud = DriverCRUD(connection)

    @staticmethod
    def driverUI(connection):
        crud = DriverCRUD(connection)
        while True:
            print("1. Add Driver Information")
            print("2. Update Driver Information")
            print("3. Delete Driver Information")
            print("4. View Driver Information")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated DriverID, Name, Handicap, Status: ").split("|")
                if len(data) != 4:
                    print('Invalid input, please enter all required fields')
                    continue
                driver_id, name, handicap, status = data
                handicap = handicap.lower() == 'true'

                if crud.addDriver(driver_id, name, handicap, status):
                    print('Operation Successful')
                else:
                    print('Operation Failed')

            elif choice == 2:
                data = input("Enter | separated DriverID, Name, Handicap, Status: ").split("|")
                if len(data) != 4:
                    print('Invalid input, please enter all required fields')
                    continue
                driver_id, name, handicap, status = data
                handicap = handicap.lower() == 'true'

                if crud.updateDriver(driver_id, name, handicap, status):
                    print('Operation Successful')
                else:
                    print('Operation Failed')

            elif choice == 3:
                driver_id = input("Enter DriverID")
                if crud.deleteDriver(driver_id):
                    print('Operation Successful')
                else:
                    print('Operation Failed')

            elif choice == 4:
                drivers = crud.viewDrivers()
                if not drivers:
                    print("No drivers to display")
                    continue
                print("| DriverID |          Name          | Handicap |     Status      |")
                print("|----------|------------------------|----------|-----------------|")
                for driver in drivers:
                    print(f"| {driver.driverID:<8} | {driver.name:<22} | {driver.handicap:<8} | {driver.status:<15} |")

            elif choice == 5:
                break
            else:
                print("Enter a valid choice")

