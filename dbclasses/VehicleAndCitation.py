# Defines the getter and setter methods for the license palte and citation to establish a relation
class VehicleAndCitation:
    def __init__(self, license_plate, citation_number):
        self.license_plate = license_plate
        self.citation_number = citation_number

    def __str__(self):
        return f'VehicleAndCitation({self.license_plate}, {self.citation_number})'

    def getLicensePlate(self):
        return self.license_plate

    def getCitationNumber(self):
        return self.citation_number

    def setLicensePlate(self, license_plate):
        self.license_plate = license_plate

    def setCitationNumber(self, citation_number):
        self.citation_number = citation_number
