from crud import PermitCRUD
from datetime import datetime
class ParkingLotUI:
    def __init__(self, connection):
        self.crud = PermitCRUD(connection)

    def permitUI(self):
        while True:
            print("1. Enter Permit Information")
            print("2. Update Permit Information")
            print("3. Delete Permit Information")
            print("4. View Permit Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated PermitID, PermitType, ExpirationTime, StartDate, EndDate: ").split('|')
                if len(data) != 5:
                    print("Enter all 5 required fields")
                    continue
                permit_id, permit_type, expiration_time, start_date, end_date = data

                expiration_time = datetime.strptime(expiration_time, '%H:%M:%S').time()
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

                if self.crud.addPermit(permit_id, permit_type, expiration_time, start_date, end_date):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 2:
                data = input("Enter | separated PermitID, PermitType, ExpirationTime, StartDate, EndDate: ").split('|')
                if len(data) != 5:
                    print("Enter all 5 required fields")
                    continue
                permit_id, permit_type, expiration_time, start_date, end_date = data

                expiration_time = datetime.strptime(expiration_time, '%H:%M:%S').time()
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

                if self.crud.updatePermit(permit_id, permit_type, expiration_time, start_date, end_date):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 3:
                permit_id = int(input("Enter PermitID: "))

                if self.crud.removePermit(permit_id):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 4:
                permits = self.crud.viewPermits()
                if not permits:
                    print("No Permits to Display")
                    continue
                print("| PermitID | PermitType | ExpirationTime | StartDate | EndDate |")
                print("|----------|------------|----------------|-----------|---------|")

                for permit in permits:
                    print(f"| {permit.permit_id}<8 | {permit.permit_type}:<10 | {permit.expiration_time}:<14 | {permit.start_date}:<9 | {permit.end_date}:<7 |")

            elif choice == 5:
                break
            else:
                print("Enter a valid choice")