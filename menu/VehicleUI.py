from crud import VehicleCRUD
class VehicleUI:
    def __init__(self, connection):
        self.crud = VehicleCRUD(connection)

    def vehicleUI(self):
        while True:
            print("1. Enter Vehicle Information")
            print("2. Update Vehicle Information")
            print("3. Delete Vehicle Information")
            print("4. View Vehicle Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated String LicenseNumber, Model, Year, Manufacturer, Color, DriverID: ").split('|')
                if len(data) != 6:
                    print('Invalid input, please enter all required fields')
                    continue
                license_number, model, year, manufacturer, color, driver_id = data

                if self.crud.addVehicle(license_number, model, year, manufacturer, color, driver_id):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 2:
                data = input("Enter | separated String LicenseNumber, Model, Year, Manufacturer, Color, DriverID: ").split('|')
                if len(data) != 6:
                    print('Invalid input, please enter all required fields')
                    continue
                license_number, model, year, manufacturer, color, driver_id = data

                if self.crud.updateVehicle(license_number, model, year, manufacturer, color, driver_id):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 3:
                license_number = input("Enter License Number: ")
                if self.crud.removeVehicle(license_number):
                    print('Operation Successful')
                else:
                    print("Operation Failed")

            elif choice == 4:
                vehicles = self.crud.viewVehicles()
                if not vehicles:
                    print("No vehicles to display")
                    continue
                print("| LicenseNumber | Model | Year | Manufacturer | Color | DriverID |")
                print("|---------------|-------|------|--------------|-------|----------|")
                for vehicle in vehicles:
                    print(f"| {vehicle.license_number:<15} | {vehicle.model:<5} | {vehicle.year:<4} | {vehicle.manufacturer:<12} | {vehicle.color:<5} | {vehicle.driver_id:<8} |")

            elif choice == 5:
                break

            else:
                print("Enter a valid choice")