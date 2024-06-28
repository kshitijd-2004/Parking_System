class Vehicle:
    def __init__(self, license_number, model, year, manufacturer, color, driver_id):
        self.license_number = license_number
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.color = color
        self.driver_id = driver_id

    def __str__(self):
        return f'Vehicle({self.license_number}, {self.model}, {self.year}, {self.manufacturer}, {self.color}, {self.driver_id})'

    def getDriverID(self):
        return self.driver_id

    def getModel(self):
        return self.model

    def getCarLicenseNumber(self):
        return self.license_number

    def getYear(self):
        return self.year

    def getManufacturer(self):
        return self.manufacturer

    def getColor(self):
        return self.color

    def setDriverID(self, DriverID):
        self.driver_id = DriverID

    def setModel(self, Model):
        self.model = Model

    def setCarLicenseNumber(self, CarLicenseNumber):
        self.license_number = CarLicenseNumber

    def setYear(self, year):
        self.year = year

    def setManufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def setColor(self, color):
        self.color = color
