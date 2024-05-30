from crud import VehicleAndCitationCRUD
class VehicleAndCitationUI:
    def __init__(self, connection):
        self.crud = VehicleAndCitationCRUD(connection)

    def vehicleAndCitationUI(self):
        while True:
            print("1. Enter Vehicle and Citation Information")
            print("2. Update Vehicle and Citation Information")
            print("3. Delete Vehicle and Citation Information")
            print("4. View Vehicle and Citation Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated String LicensePlate, CitationNumber: ").split('|')
                if len(data) != 2:
                    print('Invalid input, please enter all required fields')
                    continue
                license_plate, citation_number = data

                if self.crud.addVehicleCitation(license_plate, citation_number):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 2:
                data = input("Enter | separated String LicensePlate, CitationNumber: ").split('|')
                if len(data) != 2:
                    print('Invalid input, please enter all required fields')
                    continue
                license_plate, citation_number = data

                if self.crud.updateVehicleAndCitation(license_plate, citation_number):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 3:
                license_plate = input("Enter License Plate: ")
                citation_number = input("Enter Citation Number: ")
                if self.crud.deleteVehicleCitation(license_plate, citation_number):
                    print('Operation Successful')
                else:
                    print("Operation Failed")

            elif choice == 4:
                vehicle_citations = self.crud.viewVehicleCitations()
                if not vehicle_citations:
                    print("No vehicle and citation information to display")
                    continue
                print("| LicensePlate | CitationNumber |")
                print("|--------------|----------------|")
                for vc in vehicle_citations:
                    print(f"| {vc.license_plate:<14} | {vc.citation_number:<16} |")

            elif choice == 5:
                break

            else:
                print("Enter a valid choice")