from data.data_wrapper import Data_Wrapper
from model.voyage import Voyage
from logic.validation_check import ValidationLogic

class Voyage_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection
        self.crew_logic = None
    
    def setCrew(self, x):
        self.crew_logic = x

    def get_voyage(self, destination, departure):
        """Requests voyage for a certain destination and date from data wrapper TODO"""
        voyages = self.get_all_voyages()
        for voyage in voyages:
            if voyage.destination == destination & voyage.time_depart_destination == departure:
                return voyage
    
    def get_all_voyages(self):
        """TODO"""
        return self.data_wrapper.get_voyages_from_file()
    
    def register_voyage(self, new_voyage: Voyage):
        """Receives voyage object and forwards to data wrapper TODO"""
        voyage = self.get_voyage(new_voyage.destination, new_voyage.time_depart_destination)
        if not voyage:
            return self.data_wrapper.register_voyage(new_voyage)
        else:
            return ValidationLogic.ALREADY_IN_SYSTEM

    # def get_crew_info(self, destination, departure):
    #     """Receives destination and date and forwards to data wrapper"""
    #     return self.data_wrapper.get_information(destination, departure)

    def find_crew_for_voyage(self, departure_time):
        """Receives date, requests crew not working on that date and returns dictionary with key: job title and fills with all
        crew members separated by their job title"""
        # list of employees not working on this day - import from crew logic file and use the function there
        availability = False
        crew_not_working = self.crew_logic.availability_list(departure_time, availability)
        # make dict with key: job_title and fill with crew
        job_title = ["captain", "pilot", "head flight attendant", "extra flight attendants"]
        crew_dict = dict.fromkeys(job_title, None)
        for member in crew_not_working:
            if member.job_title in crew_dict:
                crew_dict[member.job_title].append(member)
        return crew_dict

    def add_crew_to_voyage(self, crew_dict: dict, voyage: Voyage):
        # receives crew to add
        # gets voyage from data
        for job_title, crew_member in crew_dict.items():
            setattr(voyage, job_title, crew_member)
        # returns new voyage object to data
        return voyage
    
    def add_aircraft_to_voyage(self, aircraft, destination, departure):
        """TODO"""
        # do we need to check if aircraft is already there and not allow them to replace it?
        voyage_to_add_aircraft = self.get_voyage( destination, departure)
        voyage_to_add_aircraft.aircraft = aircraft
        return voyage_to_add_aircraft

    def get_voyage_status(self, destination, departure):
        """Receives destination and data and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_status(destination, departure)

    def get_voyages_day(self, datetime):
        """Receive list from data wrapper, sorts by time and returns"""
        # sort by datetime
        # need to figure out the date for this TODO
        all_voyages = self.get_all_voyages()
        voyages_day = []
        for voyage in all_voyages:
            if voyage.date = datetime
        return self.data_wrapper.display_voyages_day(datetime)

    def display_voyages_week(self, datetime):
        """"""
        # sort by datetime TODO
        return self.data_wrapper.display_voyages_day(datetime)

    def get_voyage_schedule(self, ssn, departure):
        """Receives social security number and date and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_schedule(ssn, departure)