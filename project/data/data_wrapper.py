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
        """Adds a new destination to the file"""

        return self.destination_data.register_destination_in_file(destination)

    def get_destination_from_file(self, airport_aita):
        """Returns the destination with the reletive airport_airport_airport_iata"""

        return self.destination_data.get_destination_from_file(airport_aita)

    def get_destinations_from_file(self):
        """Returns a list of all destinations stored in the file"""

        return self.destination_data.get_destinations_from_file()
    
    def register_updated_destination_to_file(self, airport_iata):
        """Adds all the destinations in new file and swaps out the old destination for the new updated one"""
        return self.destination_data.register_updated_destination_to_file(airport_iata)
    

#crew functions

    def register_pilot_to_file(self, pilot):
        """Adds a new pilot to the file of pilots"""

        return self.crew_data.register_pilot_to_file(pilot)
    
    def register_flight_attendant_to_file(self, flight_attendant):
        """Adds a new flight attendant to the file of flight attendants"""
        
        return self.crew_data.register_flight_attendant_to_file(flight_attendant)
    
    def get_pilots_from_file(self):
        """Returns a list of all pilots stored in the file"""

        return self.crew_data.get_pilots_from_file()
    
    def get_flight_attendants_from_file(self):
        """Returns a list of all flight attendants stored in the file"""

        return self.crew_data.get_flight_attendants_from_file()
    
    def register_updated_pilot_to_file(self, pilot):
        """Adds all the pilots in new file and swaps out the old pilot for the new updated one"""

        return self.crew_data.register_updated_pilot_to_file(pilot)
    
    def register_updated_flight_attendant_to_file(self, flight_attendant):
        """Adds all the flight_attendants in new file and swaps out the old flight attendant for the new updated one"""

        return self.crew_data.register_updated_flight_attendant_to_file(flight_attendant)


#Voyage functions

    def register_voyage_to_file(self, voyage):
        """Adds a new voyage to the file"""

        return self.voyage_data.register_voyage_to_file(voyage)
    
    
    def get_future_voyages_from_file(self):
        """Returns a list of all current and future voyages stored in the file"""

        return self.voyage_data.get_future_voyages_from_file()
    

    def get_past_voyages_from_file(self):
        """Returns a list of all past voyages stored in the file"""
        
        return self.voyage_data.get_past_voyages_from_file()
    
    
    def register_updated_voyage_to_file(self, voyage):
        """Adds all the voyages in new file and swaps out the old voyage for the new updated one""""

        return self.voyage_data.register_updated_voyage_to_file(voyage)
    
    def move_voyages_done_to_file(self):
        """Moves all voyages that have already happend from the file voyages to the file voyages_done"""

        return self.voyage_data.move_voyages_done_to_file()
    

#aircraft functions
    
    def create_aircraft(self, aircraft):
        """Adds a new aircraft to the file"""
        
        return self.aircraft_data.create_aircraft(aircraft)


    