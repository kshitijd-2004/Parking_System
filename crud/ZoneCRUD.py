from dbclasses import Zone
import pymysql
class ZoneCRUD:
    def __init__(self, connection):
        self.connection = connection

    def addZone(self, zone_id, lot_name):
        if self.zoneExists(zone_id):
            print(f'Zone with Zone ID {zone_id} already exists')
            return False

        cursor = self.connection.cursor()
        query = "INSERT INTO Zones (ZoneID, LotName) VALUES (%s, %s)"
        try:
            cursor.execute(query, (zone_id,lot_name))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(f'Error: {e}')
            self.connection.rollback()
            return False
        finally:
            cursor.close()



    def viewZones(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Zones"
        cursor.execute(query)
        results = cursor.fetchall()
        zone_list = [Zone(zone_id, lot_name) for zone_id, lot_name in results]
        cursor.close()
        return zone_list


    def zoneExists(self, zone_id):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) WHERE ZoneID = %s"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result > 0