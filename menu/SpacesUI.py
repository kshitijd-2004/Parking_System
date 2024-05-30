from crud import SpacesCRUD

class SpacesUI:
    def __int__(self, connection):
        self.crud = SpacesCRUD(connection)

    def spacesUI(self):
        while True:
            print("1. Enter Spaces Information")
            print("2. Update Spaces Information")
            print("3. Delete Spaces Information")
            print("4. View Spaces Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated SpaceNumber, ZoneID, LotName, SpaceType, Availability: ").split('|')
                if len(data) != 5:
                    print("Invalid input, please enter all required fields")
                    continue
                space_number, zone_id, lot_name, space_type, availability = data

                if self.crud.addSpace(space_number, zone_id, lot_name,  space_type, availability):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            if choice == 2:
                data = input("Enter | separated SpaceNumber, ZoneID, LotName, SpaceType, Availability: ").split('|')
                if len(data) != 5:
                    print("Invalid input, please enter all required fields")
                    continue
                space_number, zone_id, lot_name, space_type, availability = data

                if self.crud.updateSpace(space_number, zone_id, lot_name, space_type, availability):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            if choice == 3:
                space_number = input("Enter Space Number: ")
                if self.crud.removeSpace(space_number):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            if choice == 4:
                spaces = self.crud.viewSpaces()
                if not spaces:
                    print("No spaces to display")
                    continue
                print("| SpaceNumber | ZoneID | LotName | SpaceType | Availability |")
                print("|-------------|--------|---------|-----------|--------------|")
                for space in spaces:
                    print(f'{space.space_number}<11 | {space.zone_id}<6 | {space.lot_name}<7 | {space.space_type}<9 | {space.availabilty}<12 |')

            elif choice == 5:
                break

            else:
                print("Enter a valid choice")