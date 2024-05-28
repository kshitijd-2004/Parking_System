# Contains the getter and setter methods for the driverID, name, handicap and status
class Driver:
    def __init__(self, driver_id, name, handicap, status):
        self.driverID = driver_id
        self.name = name
        self.handicap = handicap
        self.status = status

    # Driver getter methods
    def getDriverID(self):
        return self.driverID

    def getName(self):
        return self.name

    def getHandicap(self):
        return self.handicap

    def getStatus(self):
        return self.status

    # Set methods

    def setDriverID(self, driverID):
        self.driverID = driverID

    def setName(self, name):
        self.name = name

    def setHandicap(self, handicap):
        self.handicap = handicap

    def setStatus(self, status):
        self.status = status

