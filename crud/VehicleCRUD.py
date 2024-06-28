from dbclasses.Vehicle import Vehicle
import pymysql

class VehicleCRUD:
    def __init__(self, connection):
        self.connection = connection

    def viewVehicles(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Vehicles"
        cursor.execute(query)
        results = cursor.fetchall()
        vehicle_list = [Vehicle(license_number, model, year, manufacturer, color, driver_id) for license_number, model, year, manufacturer, color, driver_id in results]
        cursor.close()
        return vehicle_list

    def addVehicle(self, license_number, model, year, manufacturer, color, driver_id):
        
        if self.vehicleExists(license_number):
            print(f'Vehicle with car license number {license_number} already exists')
            return False

        cursor = self.connection.cursor()
        query = 'INSERT INTO Vehicles (CarLicenseNumber, Model, Year, Manufacturer, Color, DriverID) VALUES (%s, %s, %s, %s, %s, %s)'

        try:
            cursor.execute(query, (license_number, model, year, manufacturer, color, driver_id))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()


    def removeVehicle(self, license_number):

        if not self.vehicleExists(license_number):
            print(f'Vehicle with car license number {license_number} does not exist')
            return False

        cursor = self.connection.cursor()
        query = 'DELETE FROM Vehicle WHERE CarLicenseNumber = %s'

        try:
            cursor.execute(query, (license_number,))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f'Error: {e}')
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateVehicle(self, license_number, model, year, manufacturer, color, driver_id):

        if not self.vehicleExists(license_number):
            print(f'Vehicle with car license number {license_number} does not exist')
            return False

        cursor = self.connection.cursor()
        query = 'UPDATE Vehicles SET Model = %s, Year = %s, Manufacturer = %s, Color = %s, DriverID = %s WHERE CarLicenseNumber = %s'

        try:
            cursor.execute(query, (model, year, manufacturer, color, driver_id, license_number))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()


    def vehicleExists(self, license_number):
        cursor = self.connection.cursor()
        query = 'SELECT COUNT(*) FROM Vehicles WHERE CarLicenseNumber = %s'
        cursor.execute(query, (license_number,))
        results = cursor.fetchone()[0]
        cursor.close()
        return results > 0
