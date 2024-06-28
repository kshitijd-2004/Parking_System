class DriverAndPermits:
    def __init__(self, driverID, numPermits):
        self.driverID = driverID
        self.numPermits = numPermits

    def __str__(self):
        return f'DriverAndPermits({self.driverID}, {self.numPermits})'
    def getDriverID(self):
        return self.driverID

    def setDriverID(self, driverID):
        self.driverID = driverID

    def getNumPermits(self):
        return self.numPermits

    def setNumPermits(self, numPermits):
        self.numPermits = numPermits


