from dbclasses.ParkingLot import ParkingLot
import pymysql


class ParkingLotCRUD:
    def __init__(self, connection):
        self.connection = connection

    def viewParkingLots(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM ParkingLot"
        cursor.execute(query)
        results = cursor.fetchall()
        lot_list = [ParkingLot(lot_name, address) for lot_name, address in results]
        cursor.close()

        return lot_list

    def addParkingLot(self, lot_name, address):
        if self.lotExists(lot_name):
            print(f'Lot with lot name {lot_name} already exists')
            return False

        cursor = self.connection.cursor()
        query = "INSERT INTO ParkingLot (LotName, Address) VALUES (%s, %s)"

        try:
            cursor.execute(query, (lot_name, address))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f'Error: {e}')
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def removeParkingLot(self, lot_name):
        if not self.lotExists(lot_name):
            print(f'Lot with lot name {lot_name} does not exist')
            return False
        cursor = self.connection.cursor()
        query = "DELETE FROM ParkingLot WHERE LotName = %s"

        try:
            cursor.execute(query, (lot_name,))
            self.connection.commit()
            return cursor.rowcount() > 0
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateParkingLot(self, lot_name, address):
        if not self.lotExists(lot_name):
            print(f'Lot with lot name {lot_name} does not exist')
            return False
        cursor = self.connection.cursor()
        query = "UPDATE ParkingLot SET Address = %s WHERE LotName = %s"

        try:
            cursor.execute(query, (address, lot_name))
            self.connection.commit()
            return cursor.rowcount() > 0
        except pymysql.MySQLError as e:
            print(f'Error: {e}')
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def lotExists(self, lot_name):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM ParkingLot WHERE LotName = %s"
        cursor.execute(query, (lot_name,))
        result = cursor.fetchone()[0]
        cursor.close()
        return result > 0
