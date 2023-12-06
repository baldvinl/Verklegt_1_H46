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
        
    def display_destination(self, aita):
        return self.destination_data.display_destination(aita)
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    def change_ice_name(self, aita, new_ice_name):
        return self.destination_data.change_ice_name(aita, new_ice_name)

    def change_ice_number(self, aita, new_ice_number):
        return self.destination_data.change_ice_name(aita, new_ice_number)
