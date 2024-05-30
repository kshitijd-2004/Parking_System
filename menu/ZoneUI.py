from crud import ZoneCRUD
class ZoneUI:
    def __init__(self, connection):
        self.crud = ZoneCRUD(connection)

    def zoneUI(self):
        while True:
            print("1. Enter Zone Information")
            print("2. Update Zone Information")
            print("3. Delete Zone Information")
            print("4. View Zone Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated String ZoneID, LotName: ").split('|')
                if len(data) != 2:
                    print('Invalid input, please enter all required fields')
                    continue
                zone_id, lot_name = data

                if self.crud.addZone(zone_id, lot_name):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 2:
                data = input("Enter | separated String ZoneID, LotName: ").split('|')
                if len(data) != 2:
                    print('Invalid input, please enter all required fields')
                    continue
                zone_id, lot_name = data

                if self.crud.updateZone(zone_id, lot_name):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 3:
                zone_id = input("Enter Zone ID: ")
                if self.crud.removeZone(zone_id):
                    print('Operation Successful')
                else:
                    print("Operation Failed")

            elif choice == 4:
                zones = self.crud.viewZones()
                if not zones:
                    print("No zones to display")
                    continue
                print("| ZoneID | LotName |")
                print("|--------|---------|")
                for zone in zones:
                    print(f"| {zone.zone_id:<7} | {zone.lot_name:<7} |")

            elif choice == 5:
                break

            else:
                print("Enter a valid choice")