from data.voyage_data import Voyage_Data
from model.voyage import Voyage

class Voyage_Logic:
    def __init__(self, data_connection, crew_logic_instance):
        self.data_wrapper = data_connection
        self.crew_logic = None
    
    def setCrew(self, x):
        self.crew_logic = x

    def register_voyage(self, voyage):
        """Receives voyage object and forwards to data wrapper"""
        return self.data_wrapper.register_voyage(voyage)

    def get_crew_info(self, destination, date):
        """Receives destination and date and forwards to data wrapper"""
        return self.data_wrapper.get_information(destination, date)

    def get_voyage(self, destination, date):
        return self.data_wrapper.get_voyage(destination, date)

    def find_crew_for_voyage(self, datetime):
        """Receives date, requests crew not working on that date and returns dictionary with key: job title and fills with all
        crew members separated by their job title"""
        # list of employees not working on this day - import from crew logic file and use the function there
        availability = "not working"
        crew_not_working = self.crew_logic.crew_not_working(datetime, availability)
        # make dict with key: job_title and fill with crew
        job_title = ["captain", "pilot", "head flight attendant", "extra flight attendants"]
        crew_dict = dict.fromkeys(job_title, None)
        for member in crew_not_working:
            if member.job_title in crew_dict.keys():
                crew_dict[member.job_title].append(member)
        return crew_dict

    def add_crew_to_voyage(self, crew, destination, date):
        # receives crew to add
        # gets voyage from data
        # checks what is the job title of each one and adds to voyage
        # returns new voyage object to data
        pass

    def get_voyage_status(self, destination, date):
        """Receives destination and data and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_status(destination, date)

    def display_voyages_day(self, datetime):
        """Receive list from data wrapper, sorts by time and returns"""
        # sort by datetime
        return self.data_wrapper.display_voyages_day(datetime)

    def display_voyages_week(self, datetime):
        """"""
        # sort by datetime
        return self.data_wrapper.display_voyages_day(datetime)

    def get_voyage_schedule(self, ssn, date):
        """Receives social security number and date and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_schedule(ssn, date)