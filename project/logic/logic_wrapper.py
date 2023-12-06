from data.data_wrapper import Data_Wrapper
from logic.aircraft_logic import aircraft_logic
from logic.crew_logic import crew_logic
from logic.destination_logic import destination_logic
from logic.voyage_logic import voyage_logic

    # What is a good way to make changes to crew info for example? Do we need one function for each field
    # How to we write function that receives information from input 
class Logic_Wrapper:
    def __init__(self) -> None:
        self.data_wrapper = Data_Wrapper()
        self.aircraft_logic = aircraft_logic(self.data_wrapper)
        self.crew_logic = crew_logic(self.data_wrapper)
        self.destination_logic = destination_logic(self.data_wrapper)
        self.voyage_logic = voyage_logic(self.data_wrapper)

    # Register
    def register_crew(self, crew):
        """Takes crew object and forwards to data layer"""
        return crew_logic.register_crew(crew)

    def register_destination(self, destination):
        """Takes destination object and forwards to data layer"""
        return destination_logic.register_destination(destination)

    def register_voyage(self, voyage): 
        # When voyage is registered, choose aircraft first then employees
        # When voyage is registered shall prevent registering a pilot that doesn't have a type rating for an aircraft for that aircraft
        # Voyage has to consist of two flights and each flight has to be registered with different flight number
        """Takes voyage objects and forwards to data layer"""
        return voyage_logic.register_voyage(voyage)

    def register_aircraft(self, aircraft):
        """Takes aircraft objects and forwards to data layer"""
        return aircraft_logic.register_aircraft(aircraft)

    # Change information
    def change_crew_info(self, crew):
        return crew_logic.change_crew_info(crew) # TO BE DECIDED
    
    # to add -- add type rating to pilot

    def change_ice_name(self, name):
        return destination_logic.change_ice_name(name)

    def change_ice_number(self, number):
        return destination_logic.change_ice_number(number)
    
    def add_crew(self, crew, voyage):
        return voyage_logic.add_crew(crew, voyage)
    
    def add_aircraft(self, aircraft, voyage):
        return voyage_logic.add_aircraft(aircraft, voyage)

    # Display requests
        # Crew
    def display_all_crew(self):
        return crew_logic.display_all_crew()
    
    # to add -- pilots and flight attendants
    # to add -- display all pilots rated for specific aircraft
    # to add -- display all pilots sorted by aircraft type

    def get_crew_info(self, ssn):
        return crew_logic.get_crew_info(ssn)

    def display_not_working(self, day):
        return crew_logic.display_not_working(day)

    def display_working(self):
        return crew_logic.display_working()

        # Destination
    def display_destination(self, aita): # ARE WE GIVING DESTINATION AN ID?
        return destination_logic.display_destination(aita)

        # Voyage
    def display_voyage(self): # ID?
        return voyage_logic.dsplay_voyage()

    def get_voyage_status(self):
        return voyage_logic.get_voyage_status()

    def display_all_voyages_day(self, day):
        return voyage_logic.display_all_voyages_day(day)
    
    def display_all_voyages_week(self, week): # should we have weeks numbered like in the calendar?
        return voyage_logic.display_all_voyages_week(week)
    
    def get_voyage_schedule(self, crew, day):
        return voyage_logic.get_voyage_schedule(crew, day)

        # Aircraft
    def display_aircraft_info(self): # ID?
        return aircraft_logic.display_aircraft_info()

    def get_aircraft_status(self):
        return aircraft_logic.get_aircraft_status()
    
    def display_all_aircrafts(self, day, time):
        return aircraft_logic.display_all_aircrafts(day, time)