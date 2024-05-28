class Spaces:
    def __init__(self, space_number, zone_id, lot_name,  space_type, availability):
        self.space_number = space_number
        self.zone_id = zone_id
        self.lot_name = lot_name
        self.space_type = space_type
        self.availability = availability


    def getSpaceNumber(self):
        return self.space_number

    def getZoneID(self):
        return self.zone_id

    def getLotName(self):
        return self.lot_name

    def getSpaceType(self):
        return self.space_type

    def getAvailability(self):
        return self.availability

    def setZoneID(self, zone_id):
        self.zone_id = zone_id

    def setLotName(self, lot_name):
        self.lot_name = lot_name

    def setSpaceNumber(self, space_number):
        self.space_number = space_number

    def setSpaceType(self, space_type):
        self.space_type = space_type

    def setAvailability(self, availability):
        self.availability = availability

        