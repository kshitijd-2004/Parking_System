from dbclasses import VehicleAndCitation
import pymysql

class VehicleAndCitationCRUD:
    def __init__(self, connection):
        self.connection = connection

    def addVehicleCitation(self, license_number, citation_number):
        if self.linkExists(license_number, citation_number):
            print(f"Link between {license_number} and {citation_number} already exists")
            return False
        cursor = self.connection.cursor()
        query = "INSERT INTO VehicleCitations (CarLicenseNumber, CitationNumber) VALUES (%s, %s)"

        try:
            cursor.execute(query, (license_number, citation_number))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def deleteVehicleCitation(self, license_number, citation_number):
        if not self.linkExists(license_number, citation_number):
            print(f"Link between {license_number} and {citation_number} does not exist")
            return False

        cursor = self.connection.cursor()
        query = "DELETE FROM VehicleCitations WHERE CarLicenseNumber = %s AND CitationNumber = %s"

        try:
            cursor.execute(query, (license_number, citation_number))
            self.connection.commit()
            return cursor.rowcount() > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            return False
        finally:
            cursor.close()

    def viewVehicleCitations(self):
        cursor = self.connection.cursor
        query = "SELECT * FROM VehicleCitations"
        cursor.execute(query)
        results = cursor.fetchall()
        vehiclecitations_list = [VehicleAndCitation(license_number, citation_number) for license_number, citation_number in results]
        cursor.close()
        return vehiclecitations_list

    def linkExists(self, license_number, citation_number):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM VehicleCitations WHERE license_number = %s AND citation_number = %s"
        cursor.execute(query, (license_number, citation_number))
        result = cursor.fetchone()[0]
        return result > 0
