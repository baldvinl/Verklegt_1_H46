from data.data_wrapper import Data_Wrapper
from logic.aircraft_logic import Aircraft_Logic
from logic.crew_logic import Crew_Logic
from logic.destination_logic import Destination_Logic
from logic.voyage_logic import Voyage_Logic

    # What is a good way to make changes to crew info for example? Do we need one function for each field
    # How to we write function that receives information from input 
class Logic_Wrapper:
    def __init__(self) -> None:
        self.data_wrapper = Data_Wrapper()
        self.aircraft_logic = Aircraft_Logic(self.data_wrapper)
        self.crew_logic = Crew_Logic(self.data_wrapper)
        self.destination_logic = Destination_Logic(self.data_wrapper)
        self.voyage_logic = Voyage_Logic(self.data_wrapper)

    # Register
    def register_crew(self, crew):
        """Takes crew object and forwards to data layer"""
        return Crew_Logic.register_crew(crew)

    def register_destination(self, destination):
        """Takes destination object and forwards to data layer"""
        return Destination_Logic.register_destination(destination)

    def register_voyage(self, voyage): 
        # When voyage is registered, choose aircraft first then employees
        # When voyage is registered shall prevent registering a pilot that doesn't have a type rating for an aircraft for that aircraft
        # Voyage has to consist of two flights and each flight has to be registered with different flight number
        """Takes voyage objects and forwards to data layer"""
        return Voyage_Logic.register_voyage(voyage)

    def register_aircraft(self, aircraft):
        """Takes aircraft objects and forwards to data layer"""
        return Aircraft_Logic.register_aircraft(aircraft)

    # Change information
    def change_crew_info(self, crew):
        return Crew_Logic.change_crew_info(crew) # TO BE DECIDED
    
    # to add -- add type rating to pilot

    def change_ice_name(self, name):
        return Destination_Logic.change_ice_name(name)

    def change_ice_number(self, number):
        return Destination_Logic.change_ice_number(number)
    
    def add_crew(self, crew, voyage):
        return Voyage_Logic.add_crew(crew, voyage)
    
    def add_aircraft(self, aircraft, voyage):
        return Voyage_Logic.add_aircraft(aircraft, voyage)

    # Display requests
        # Crew
    def display_all_crew(self):
        return Crew_Logic.display_all_crew()
    
    # to add -- pilots and flight attendants
    # to add -- display all pilots rated for specific aircraft
    # to add -- display all pilots sorted by aircraft type

    def get_crew_info(self, ssn):
        return Crew_Logic.get_crew_info(ssn)

    def display_not_working(self, day):
        return Crew_Logic.display_not_working(day)

    def display_working(self):
        return Crew_Logic.display_working()

        # Destination
    def display_destination(self): # ARE WE GIVING DESTINATION AN ID?
        return Destination_Logic.display_destination()

        # Voyage
    def display_voyage(self): # ID?
        return Voyage_Logic.dsplay_voyage()

    def get_voyage_status(self):
        return Voyage_Logic.get_voyage_status()

    def display_all_voyages_day(self, day):
        return Voyage_Logic.display_all_voyages_day(day)
    
    def display_all_voyages_week(self, week): # should we have weeks numbered like in the calendar?
        return Voyage_Logic.display_all_voyages_week(week)
    
    def get_voyage_schedule(self, crew, day):
        return Voyage_Logic.get_voyage_schedule(crew, day)

        # Aircraft
    def display_aircraft_info(self): # ID?
        return Aircraft_Logic.display_aircraft_info()

    def get_aircraft_status(self):
        return Aircraft_Logic.get_aircraft_status()
    
    def display_all_aircrafts(self, day, time):
        return Aircraft_Logic.display_all_aircrafts(day, time)