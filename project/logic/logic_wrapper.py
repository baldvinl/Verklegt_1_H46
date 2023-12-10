from data.data_wrapper import Data_Wrapper
from logic.aircraft_logic import Aircraft_Logic
from logic.crew_logic import Crew_Logic
from logic.destination_logic import Destination_Logic
from logic.voyage_logic import Voyage_Logic

from model.aircraft import Aircraft
from model.crew import Crew
from model.destination import Destination
from model.flight_attendant import Flight_Attendant
from model.pilot import Pilot
from model.voyage import Voyage

class Logic_Wrapper:
    def __init__(self) -> None:
        self.data_wrapper = Data_Wrapper()
        self.aircraft_logic = Aircraft_Logic(self.data_wrapper)
        self.crew_logic = Crew_Logic(self.data_wrapper)
        self.destination_logic = Destination_Logic(self.data_wrapper)
        self.voyage_logic = Voyage_Logic(self.data_wrapper) #, self.crew_logic)
        self.voyage_logic.setCrew(self.crew_logic)
        self.crew_logic.setVoyage(self.voyage_logic) # needs to be fixed

    # CREW
    def register_crew(self, crew: Crew):
        """Receives crew object, checks if it's a pilot or 
        a flight attendant and forwards to data wrapper accordingly"""
        crew_info = self.crew_logic.register_crew(crew)
        return crew_info

    def change_crew_info(self, ssn: str, changes: list[tuple]):
        """Receives ssn of crew member and changes in a list of tuples
        with the format [(attribute, new_value)], requests crew member with
        provided ssn from data wrapper, makes the changes and sends back
        the updated crew member object."""
        return self.crew_logic.change_crew_info(ssn, changes)
    
    def display_crew_member(self, ssn: str):
        """Receives social security number of employee and forwards to data wrapper"""
        return self.crew_logic.get_crew_member(ssn)

    def display_all_crew(self):
        """Receives request, asks for list of pilots and flight attendants from data
        wrapper, combines both into one list and returns it"""
        all_crew_list = self.crew_logic.get_all_crew()
        return all_crew_list

    def availability_list(self, date, availability): # to be implemented in ui still
        """Receives date and availability request (working or not working), requests
        voyages that day using the date from data wrapper, gets all crew from data wrapper. Using
        the ssns found in the voyages that day it makes 2 lists one for crew thats working
        and one for crew that isnt. Then returns according to the availability requested"""
        crew_list = self.crew_logic.availability_list(date, availability)
        return crew_list
    
    def display_pilots(self):
        """Receives request, gets pilots list from data and returns it"""
        pilots_list = self.crew_logic.get_pilots()
        return pilots_list
    
    def display_flight_attendants(self):
        """Receives request, gets flight attendants list from data and returns it"""
        flight_attendants_list = self.crew_logic.get_flight_attendants()
        return flight_attendants_list
    
    # to add -- add type rating to pilot
    # to add -- display all pilots rated for specific aircraft
    # to add -- display all pilots sorted by aircraft type

    # AIRCRAFT

    def register_aircraft(self, aircraft):
        """Receives aircraft objects and forwards to data wrapper"""
        return self.aircraft_logic.register_aircraft(aircraft)

    def display_aircraft_info(self, name):
        """Receives aircrafts name and forwards it to data wrapper"""
        return self.aircraft_logic.display_aircraft_info(name)

    def get_aircraft_status(self, name):
        """Receives aircrafts name and forwards it to data wrapper"""
        return self.aircraft_logic.get_aircraft_status(name)
    
    def display_all_aircrafts(self, date, time):
        """Receives date and time and forwards them to data wrapper"""
        return self.aircraft_logic.display_all_aircrafts(date, time)
    
    # VOYAGE

    def register_voyage(self, voyage): 
        # When voyage is registered, choose aircraft first then employees
        # When voyage is registered shall prevent registering a pilot that doesn't have a type rating for an aircraft for that aircraft
        # Voyage has to consist of two flights and each flight has to be registered with different flight number
        """Receives voyage objects and forwards to data wrapper"""
        return self.voyage_logic.register_voyage(voyage)
    
    def add_aircraft(self, aircraft, voyage):
        """"""
        return self.voyage_logic.add_aircraft(aircraft, voyage)
    
    def display_voyages_day(self, datetime):
        """Receives selected date and forwards it to data wrapper"""
        return self.voyage_logic.display_voyages_day(datetime)
    
    def display_voyages_week(self, datetime):
        """Receives selected week and forwards it to data wrapper"""
        return self.voyage_logic.display_voyages_week(datetime)
    
    def get_voyage_schedule(self, ssn, date):
        """Receives employees social security number and date selected and forwards to data wrapper"""
        return self.voyage_logic.get_voyage_schedule(ssn, date)
    
    def get_voyage_status(self, destination, date):
        """Receives destination and date and forwards them to data wrapper"""
        return self.voyage_logic.get_voyage_status(destination, date)
    
    def add_crew(self, crew, voyage):
        """"""
        return self.voyage_logic.add_crew(crew, voyage)
    
    # DESTINATION
    def register_destination(self, destination):
        """Receives destination object and forwards to data wrapper"""
        return self.destination_logic.register_destination(destination)

    def change_ice_name(self, name):
        """"""
        return self.destination_logic.change_ice_name(name)

    def change_ice_number(self, number):
        """"""
        return self.destination_logic.change_ice_number(number)
    
    def display_destinations(self):
        """Forwards request to data wrapper"""
        return self.destination_logic.display_destinations()