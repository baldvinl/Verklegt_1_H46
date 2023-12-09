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

    def find_crew_for_voyage(self, destination, datetime):
        """"""
        # to do later - aircraft needs to be added before crew later in B requirements - check if aircraft in voyage validation
        voyage = self.data_wrapper.get_voyage(destination, datetime) # to replace
        # get voyage object from data with the input information
        # list of employees not working on this day - import from crew logic file and use the function there
        # make and lists inside of list, separated by job title [captain, pilot, head flight attendant]
        # return list of lists and voyage obj
        pass

    def add_crew_to_voyage(self, crew, voyage):
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