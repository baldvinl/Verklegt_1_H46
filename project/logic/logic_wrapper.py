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
        self.voyage_logic = Voyage_Logic(self.data_wrapper)
        self.crew_logic = Crew_Logic(self.data_wrapper, self.voyage_logic)
        self.destination_logic = Destination_Logic(self.data_wrapper) #Took out the voyage_logic to be able to run

    # CREW

    def get_crew_member(self, ssn: str):
        """Receives social security number of crew member, checks if already exists and forwards to data wrapper
        if not it returns an error code"""
        return self.crew_logic.get_crew_member(ssn)

    def register_crew(self, crew: Crew):
        """Receives crew object, checks if member with same ssn already exists, if not checks 
        if crew object received is of the type Pilot or not and forwards to data wrapper accordingly"""
        return self.crew_logic.register_crew(crew)

    def change_crew_info(self, crew_member):
        """Receives ssn of crew member and changes in a list of tuples
        with the format [(attribute, new_value)], requests crew member with
        provided ssn from data wrapper, makes the changes and sends back
        the updated crew member object."""
        return self.crew_logic.change_crew_info(crew_member)

    def get_all_crew(self):
        """Receives lists of pilots and flight attendants 
        from data wrapper, combines them and returns list if not empty, otherwise an error code"""
        return self.crew_logic.get_all_crew()

    def crew_status(self, date, busy: bool): #TODO
        """Receives date and availability request (working or not working), requests
        voyages that day using the date from data wrapper, gets all crew from data wrapper. Using
        the ssns found in the voyages that day it makes 2 lists one for crew thats working
        and one for crew that isnt. Then returns according to the availability requested"""
        return self.crew_logic.crew_status(date, busy)
    
    def get_pilots(self):
        """Requests all pilots from data wrapper and returns if there is any. 
        If not returns error code"""
        return self.crew_logic.get_pilots()
    
    def get_flight_attendants(self):
        """Requests all flight attendants from data wrapper and returns if there is any. 
        If not returns error code"""
        return self.crew_logic.get_flight_attendants()
    
    def find_crew_for_voyage(self, departure_time):
        """Receives date, requests crew not working on that date, returns dictionary with key: job title 
        and fills with all crew members separated by their job title, if there is no crew it returns
        error code"""
        return self.crew_logic.find_crew_for_voyage(departure_time)

    # AIRCRAFT

    def register_aircraft(self, aircraft: Aircraft):
        """Receives aircraft objects and forwards to data wrapper"""
        return self.aircraft_logic.register_aircraft(aircraft)

    def display_aircraft_info(self, name: str):
        """Receives aircrafts name and forwards it to data wrapper"""
        return self.aircraft_logic.get_aircraft_info(name)

    def display_aircraft_status(self, name: str):
        """Receives aircrafts name and forwards it to data wrapper"""
        return self.aircraft_logic.get_aircraft_status(name)
    
    def display_all_aircrafts(self, datetime):
        """Receives datetime, requests aicrafts from data and returns the list"""
        return self.aircraft_logic.get_all_aircrafts(datetime)
    
    # VOYAGE

    def voyage_files_maintenance(self):
        """Forwards request to data wrapper"""
        return self.voyage_logic.voyage_files_maintenance()

    def get_voyage(self, destination: str, departure):
        """Requests voyage list, checks for a certain voyage with specific destination 
        and departure time from data wrapper, returns either voyage object or error code"""
        return self.voyage_logic.get_voyage(destination, departure)
    
    def get_all_voyages(self):
        """Requests voyage list from data wrapper, checks if empty, if so returns error otherwise returns list"""
        return self.voyage_logic.get_all_voyages()

    def register_voyage(self, new_voyage: Voyage):
        """Receives voyage object, checks if already in system, if so returns error code
        and if not forwards to data wrapper"""
        return self.voyage_logic.register_voyage(new_voyage)
    
    def add_crew_to_voyage(self, crew_dict: dict, voyage: Voyage):
        """Receives crew dictionary separated by job titles, adds to voyage object receives and returns
        to data wrapper"""
        return self.voyage_logic.add_crew_to_voyage(crew_dict, voyage)
    
    def add_aircraft_to_voyage(self, aircraft, destination, departure):
        """Gets voyage with certain destination & departure time, adds aircraft to it and returns to data wrapper"""
        return self.voyage_logic.add_aircraft_to_voyage(aircraft, destination, departure)
    
    def get_voyage_status(self, destination, date):
        """Receives destination and date and forwards them to data wrapper TODO B requirement"""
        return self.voyage_logic.get_voyage_status(destination, date)
    
    def get_voyages_for_period(self, starting_date, total_days):
        """Receives a starting date in datetime format, and total days of voyages to return. Requests all voyages from data wrapper
        makes a list of all the dates to be included in the final list. Goes through all voyages and keeps only the ones with the same dates.
        Sorts by departure time and returns list. If no voyages were initially received from data wrapper, it raises an error"""
        return self.voyage_logic.get_voyages_for_period(starting_date, total_days)
    
    def get_weekly_voyage_schedule(self, ssn_and_date):
        """Receives ssn, and starting date of the week, checks them for the crew members ssn, and saves
        the one that have them listed. returns them in a list sorted. if there is no voyages it returns error code"""
        return self.voyage_logic.get_weekly_voyage_schedule(ssn_and_date)
    
    # DESTINATION

    def register_destination(self, destination: Destination):
        """Receives destination, checks if it already exists, if so gives error, if not it forwards
        the new destination to data wrapper."""
        return self.destination_logic.register_destination(destination)
    
    def get_destination(self, iata: str):
        """Requests lists of all destinations from data wrapper. If empty it returns an error
        if not it finds specific destination with iata provided and returns it."""
        return self.destination_logic.get_destination(iata)
    
    def get_all_destinations(self):
        """Forwards request to data wrapper"""
        return self.destination_logic.get_all_destinations()
    
    def change_emergency_contact_info(self, airport: str, new_info: tuple):
        """Receives iata and new_info tuple with the format (new_name, new_number) - if one of those doesn't need to be changed
        it will be set to "None", requests destination object from data
        wrapper using iata, changes the information and returns updated destination object"""
        return self.destination_logic.change_emergency_contact_info(airport, new_info)