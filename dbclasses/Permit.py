class Permit:
    def __init__(self, permit_id, permit_type, expiration_time, start_date, end_date):
        self.permit_id = permit_id
        self.permit_type = permit_type
        self.expiration_time = expiration_time
        self.start_date = start_date
        self.end_date = end_date

    def getPermitID(self):
        return self.permit_id

    def getPermitType(self):
        return self.permit_type

    def getExpirationTime(self):
        return self.expiration_time

    def getStartDate(self):
        return self.start_date

    def getEndDate(self):
        return self.end_date

    def setPermitID(self, permit_id):
        self.permit_id = permit_id

    def setPermitType(self, permit_type):
        self.permit_type = permit_type

    def setExpirationTime(self, expiration_time):
        self.expiration_time = expiration_time

    def setStartDate(self, start_date):
        self.start_date = start_date

    def setEndDate(self, end_date):
        self.end_date = end_date
