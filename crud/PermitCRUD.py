from dbclasses import Permit
import pymysql
class PermitCRUD:
    def __init__(self, connection):
        self.connection = connection

    def viewPermits(self):
        cursor = self.connection.cursor()
        query = 'SELECT * FROM Permits'
        cursor.execute(query)
        results = cursor.fetchall()
        permit_list = [Permit(permit_id, permit_type, expiration_time, start_date, end_date) for  permit_id, permit_type, expiration_time, start_date, end_date in results]
        cursor.close()
        return permit_list

    def addPermit(self, permit_id, permit_type, expiration_time, start_date, end_date):
        if self.permitExists(permit_id):
            print(f'Permit with {permit_id} already exists')
            return False
        cursor = self.connection.cursor()
        query = "INSERT INTO Permits (PermitID, PermitType, ExpirationTime, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (permit_id, permit_type, expiration_time, start_date, end_date))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def removePermit(self, permit_id):
        if not self.permitExists(permit_id):
            print(f'Permit with {permit_id} does not exist')
            return False
        cursor = self.connection.cursor()
        query = 'DELETE FROM Permits WHERE PermitID = %s'
        try:
            cursor.execute(query, (permit_id))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()


    def updatePermit(self, permit_id, permit_type, expiration_time, start_date, end_date):
        if not self.permitExists(permit_id):
            print(f'Permit with {permit_id} does not exist')
            return False
        cursor = self.connection.cursor()
        query = "UPDATE Permits SET PermitType = %s, ExpirationTime = %s, StartDate = %s, EndDate = %s"

        try:
            cursor.execute(query, (permit_type, expiration_time, start_date, end_date, permit_id))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def permitExists(self, permit_id):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM Permits WHERE PermitID = %s"

        cursor.execute(query, (permit_id,))
        results = cursor.fetchone()[0]
        cursor.close()
        return results > 0