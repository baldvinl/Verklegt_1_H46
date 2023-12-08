from data.voyage_data import Voyage_Data
from model.voyage import Voyage

class Voyage_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_voyage(self, voyage):
        """Receives voyage object and forwards to data wrapper"""
        return self.data_wrapper.register_voyage(voyage)

    def get_crew_info(self, destination, date):
        """Receives destination and date and forwards to data wrapper"""
        return self.data_wrapper.get_information(destination, date)

    def add_crew(self, crew, voyage):
        """"""
        return self.data_wrapper.add_crew(crew, voyage)

    def get_voyage_status(self, destination, date):
        """Receives destination and data and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_status(destination, date)

    def display_voyages_day(self, date):
        """Receive list from data wrapper, sorts by time and returns"""
        # sort by time ascending
        return self.data_wrapper.display_voyages_day(date)

    def display_voyages_week(self, date):
        """"""
        # sort by date and time?
        return self.data_wrapper.display_voyages_day(date)

    def get_voyage_schedule(self, ssn, date):
        """Receives social security number and date and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_schedule(ssn, date)