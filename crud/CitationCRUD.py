from dbclasses.Citation import Citation
import pymysql


class CitationCRUD:
    def __init__(self, connection):
        self.connection = connection

    def viewCitations(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Citation"
        cursor.execute(query)
        results = cursor.fetchall()
        citations_list = [
            Citation(citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category)
            for citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category in
            results]
        cursor.close()
        return citations_list

    def addCitation(self, citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name,
                    category):
        cursor = self.connection.cursor()
        query = "INSERT INTO Citation (CitationNumber, PaymentStatus, AppealStatus, CitationDate, CitationTime, LotName, Category) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        try:
            cursor.execute(query, (
            citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category))
            self.connection.commit()
            return True
        except pymysql.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def removeCitation(self, citation_number):
        cursor = self.connection.cursor()
        query = "DELETE FROM Citation WHERE citation_number = %s"

        try:
            cursor.execute(query, (citation_number,))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def updateCitation(self, citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category):
        cursor = self.connection.cursor()
        query = "UPDATE Citation SET PaymentStatus = %s, AppealStatus = %s, CitationDate = %s, CitationTime = %s, LotName = %s, Category = %s WHERE CitationNumber = %s"

        try:
            cursor.execute(query, (payment_status, appeal_status, citation_date, citation_time, lot_name, category, citation_number))
            self.connection.commit()
            return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f'Error: {e}')
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def citationExists(self, citation_number):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM Citation WHERE citation_number = %s"

        cursor.execute(query, (citation_number,))

        result = cursor.fetchone()[0]
        cursor.close()
        return result > 0
