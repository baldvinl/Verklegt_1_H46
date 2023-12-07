from data.destination_data import Destination_Data
from data.aircraft_data import Aircraft_Data
from data.crew_data import Crew_Data
from data.voyage_data import Voyage_Data


class Data_Wrapper:
    def __init__(self):
        self.destination_data = Destination_Data()
        self.crew_data = Crew_Data()
        self.aircraft_data = Aircraft_Data()
        self.voyage_data = Voyage_Data()


#destination functions

    def display_destinations(self):
        return self.destination_data.display_destinations()
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    def change_ice_name(self, iata, new_ice_name):
        return self.destination_data.change_ice_name(iata, new_ice_name)

    def change_ice_number(self, iata, new_ice_number):
        return self.destination_data.change_ice_name(iata, new_ice_number)
    

#crew functions

    def register_pilot(self, pilot):
        return self.crew_data.register_pilot(pilot)
    
    def register_flight_attendant(self, flight_attendant):
        return self.crew_data.register_flight_attendant(flight_attendant)
    

#Voyage functions

    def create_voyage(self, voyage):
        return self.voyage_data.create_voyage(voyage)
    

#aircraft functions
    
    def create_aircraft(self, aircraft):
        return self.aircraft_data.create_aircraft(aircraft)


    