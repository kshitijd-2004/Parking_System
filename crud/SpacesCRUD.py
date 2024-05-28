from dbclasses import Spaces
import pymysql
class SpacesCRUD:
    def __init__(self, connection):
        self.connection = connection

    def viewSpaces(self):
        cursor = self.connection.cursor()
        query = 'SELECT * FROM Spaces'
        cursor.execute(query)
        results = cursor.fetchall()
        spaces_list = [Spaces(space_number, zone_id, lot_name,  space_type, availability) for space_number, zone_id, lot_name,  space_type, availability in results]
        cursor.close()
        return spaces_list

    def addSpace(self, space_number, zone_id, lot_name,  space_type, availability):
        if self.spaceExists(space_number):
            print(f'Space with space number {space_number} already exists')
            return False
        cursor = self.connection.cursor()
        query = 'INSERT INTO Spaces (SpaceNumber, ZoneID, LotName, SpaceType, Availability) VALUES (%s, %s, %s, %s, %s)'

        try:
            cursor.execute(query, (space_number, zone_id, lot_name,  space_type, availability))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f'Error: {e}')
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def removeSpace(self, space_number):
        if not self.spaceExists(space_number):
            print(f'Space with space number {space_number} does not exist')
            return False
        cursor = self.connection.cursor()
        query = 'DELETE FROM Spaces WHERE SpaceNumber = %s'
        try:
            cursor.execute(query, (space_number))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateSpace(self,  space_number, zone_id, lot_name,  space_type, availability):
        if not self.spaceExists(space_number):
            print(f'Space with space number {space_number} does not exist')
            return False
        cursor = self.connection.cursor()
        query = "UPDATE Spaces SET ZoneID = %s, LotName = %s, SpaceType = %s, Availability = %s WHERE SpaceNumber = %s"

        try:
            cursor.execute(query, (zone_id, lot_name,  space_type, availability, space_number))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def spaceExists(self, space_number):
        cursor = self.connection.cursor()
        query = 'SELECT COUNT(*) FROM Spaces WHERE SpaceNumber = %s'
        cursor.execute(query, (space_number,))
        results = cursor.fetchone()[0]
        cursor.close()
        return results > 0