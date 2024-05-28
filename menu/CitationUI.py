from crud import CitationCRUD
import pymysql
from datetime import datetime

class CitationUI:
    def __init__(self, connection):
        self.crud = CitationCRUD(connection)

    def citationUI(self):
        while True:
            print("1. Enter Citation Information")
            print("2. Update Citation Information")
            print("3. Delete Citation Information")
            print("4. View Citation Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if not choice.isdigit():
                print("Enter a choice number from 1 to 5")
                continue

            choice = int(choice)

            if choice == 1:
                data = input("Enter | separated String CitationNumber, PaymentStatus, AppealStatus, CitationDate, CitationTime, LotName, Category: ").split('|')
                if len(data) != 7:
                    print('Invalid input, please enter all required fields')
                    continue
                citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category = data

                appeal_status = appeal_status.lower() == 'true'
                citation_date = datetime.strptime(citation_date, '%Y-%m-%d').date()
                citation_time = datetime.strptime(citation_time, '%H:%M:%S').time()

                if self.crud.addCitation(citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 2:
                data = input(
                    "Enter | separated String CitationNumber, PaymentStatus, AppealStatus, CitationDate, CitationTime, LotName, Category: ").split(
                    '|')
                if len(data) != 7:
                    print('Invalid input, please enter all required fields')
                    continue
                citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category = data

                appeal_status = appeal_status.lower() == 'true'
                citation_date = datetime.strptime(citation_date, '%Y-%m-%d').date()
                citation_time = datetime.strptime(citation_time, '%H:%M:%S').time()

                if self.crud.updateCitation(citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category):
                    print("Operation Successful")
                else:
                    print("Operation Failed")

            elif choice == 3:
                citation_number = input("Enter Citation Number: ")
                if self.crud.removeCitation(citation_number):
                    print('Operation Successful')
                else:
                    print("Operation Failed")

            elif choice == 4:
                citations = self.crud.viewCitations()
                if not citations:
                    print("No citations to display")
                    continue
                print("| CitationNumber | PaymentStatus | AppealStatus | CitationDate | CitationTime | LotName | Category |")
                print( "|----------------|---------------|--------------|--------------|--------------|---------|----------|")
                for citation in citations:
                    print(f"| {citation.citation_number:<14} | {citation.payment_status:<13} | {str(citation.appeal_status):<12} | {citation.citation_date:<12} | {citation.citation_time:<12} | {citation.lot_name:<7} | {citation.category:<8} |")

            elif choice == 5:
                break

            else:
                print("Enter a valid choice")









