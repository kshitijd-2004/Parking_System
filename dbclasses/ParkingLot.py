class ParkingLot:
    def __init__(self, lot_name, address):
        self.lot_name = lot_name
        self.address = address

    def getLotName(self):
        return self.lot_name

    def getAddress(self):
        return self.address

    def setLotName(self, lot_name):
        self.lot_name = lot_name

    def setAddress(self, address):
        self.address = address
