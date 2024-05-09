class Citation1:
    def __init__(self, citation_number, payment_status, appeal_status, citation_date, citation_time, lot_name, category):
        self.citation_number = citation_number
        self.payment_status = payment_status
        self.appeal_status = appeal_status
        self.citation_date = citation_date
        self.citation_time = citation_time
        self.lot_name = lot_name
        self.category = category

        def getCitationNumber(self):
            return self.citation_number

        def getPaymentStatus(self):
            return self.payment_status

        def getAppealStatus(self):
            return self.appeal_status

        def getCitationDate(self):
            return self.citation_date

        def getCitationTime(self):
            return self.citation_time

        def getLotName(self):
            return self.lot_name

        def getCategory(self):
            return self.category

        def setCitationNumber(self, citation_number):
            self.citation_number = citation_number

        def setPaymentStatus(self, payment_status):
            self.payment_status = payment_status

        def setAppealStatus(self, appeal_status):
            self.appeal_status = appeal_status

        def setCitationDate(self, citation_date):
            self.citation_date = citation_date

        def setCitationTime(self, citation_time):
            self.citation_time = citation_time

        def setLotName(self, lot_name):
            self.lot_name = lot_name

        def setCategory(self, category):
            self.category = category