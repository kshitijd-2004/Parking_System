from dbclasses.Driver import Driver
import pymysql


class DriverCRUD:
    def __init__(self, connection):
        self.connection = connection

    def addDriver(self, driver_id, name, handicap, status):
        if self.driverExists(driver_id):
            print(f"Driver with ID {driver_id} already exists")
            return False

        cursor = self.connection.cursor()
        query = "INSERT INTO Driver (DriverID, Name, Handicap, Status) VALUES  (%s, %s, %s, %s)"

        try:
            cursor.execute(query, (driver_id, name, handicap, status))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def deleteDriver(self, driver_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM Driver WHERE DriverID = %s"

        try:
            cursor.execute(query, (driver_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateDriver(self, driver_id, name, handicap, status):

        if not self.driverExists(driver_id):
            print(f"Driver with {driver_id} does not exist")
            return False

        cursor = self.connection.cursor()
        query = "UPDATE Driver SET Name = %s, Handicap = %s, Status = %s WHERE DriverID = %s"

        try:
            cursor.execute(query, (name, handicap, status, driver_id))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Exception: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def viewDrivers(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Driver"
        cursor.execute(query)
        result = cursor.fetchall()
        driver_list = [Driver(driver_id, name, handicap, status) for driver_id, name, handicap, status in result]
        cursor.close()
        return driver_list

    def driverExists(self, driver_id):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM Driver WHERE DriverID = %s"

        try:
            cursor.execute(query, (driver_id,))
            result = cursor.fetchone()[0]
            return result > 0
        finally:
            cursor.close()