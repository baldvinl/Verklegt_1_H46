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

    def register_destination_in_file(self, destination):
        return self.destination_data.register_destination_in_file(destination)

    def get_destination_from_file(self, aita):
        return self.destination_data.get_destination_from_file(aita)

    def get_destinations_from_file(self):
        return self.destination_data.get_destinations_from_file()
    
    def register_updated_destination_to_file(self, iata):
        return self.destination_data.register_updated_destination_to_file(iata)
    

#crew functions

    def register_pilot_to_file(self, pilot):
        return self.crew_data.register_pilot_to_file(pilot)
    
    def register_flight_attendant_to_file(self, flight_attendant):
        return self.crew_data.register_flight_attendant_to_file(flight_attendant)
    
    def get_pilots_from_file(self):
        return self.crew_data.get_pilots_from_file()
    
    def get_flight_attendants_from_file(self):
        return self.crew_data.get_flight_attendants_from_file()
    
    def get_crew_member_from_file(self, ssn):
        return self.crew_data.get_crew_member_from_file(ssn)
    
    def change_pilot_info(self, ssn, changes):
        return self.crew_data.change_pilot_info(ssn, changes)
    
    def change_flight_attendant_info(self, ssn, changes):
        return self.crew_data.change_flight_attendant_info(ssn, changes)


#Voyage functions

    def create_voyage(self, voyage):
        return self.voyage_data.create_voyage(voyage)
    

#aircraft functions
    
    def create_aircraft(self, aircraft):
        return self.aircraft_data.create_aircraft(aircraft)


    