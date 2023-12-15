class Destination:
    def __init__(self, airport=None, country=None, flight_duration=None, distance=None, ice_name=None, ice_number=None):
        self.airport = airport
        self.country = country
        self.flight_duration = flight_duration
        self.distance = distance
        self.ice_name = ice_name
        self.ice_number = ice_number

    def attribute_implementation(self, attributes_list):
        self.airport = attributes_list[0]
        self.country = attributes_list[1]
        self.flight_duration = attributes_list[2]
        self.distance = attributes_list[3]
        self.ice_name = attributes_list[4]
        self.ice_number = attributes_list[5]
