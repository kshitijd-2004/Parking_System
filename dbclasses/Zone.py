class Zone:
    def __init__(self, zone_id, lot_name):
        self.zone_id = zone_id
        self.lot_name = lot_name

    def __str__(self):
        return f'Zone({self.zone_id}, {self.lot_name})'

    def get_zone_id(self):
        return self.zone_id

    def get_lot_name(self):
        return self.lot_name

    def set_zone_id(self, zone_id):
        self.zone_id = zone_id

    def set_lot_name(self, lot_name):
        self.lot_name = lot_name
