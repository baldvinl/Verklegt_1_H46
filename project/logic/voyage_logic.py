from data.voyage_data import Voyage_Data
from model.voyage import Voyage

class Voyage_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_voyage(self, voyage):
        return self.data_wrapper.register_voyage(voyage)

    def get_crew_info(self, destination, date):
        return self.data_wrapper.get_information(destination, date)

    def add_crew(self, crew, voyage):
        return self.data_wrapper.add_crew(crew, voyage)

    def get_voyage_status(self, destination, date):
        return self.data_wrapper.get_voyage_status(destination, date)

    def display_all_voyages_day(self, date):
        return self.data_wrapper.display_all_voyages_day(date)

    def display_all_voyages_week(self, date):
        return self.data_wrapper.display_all_voyages_day(date)

    def get_voyage_schedule(self, ssn, date):
        return self.data_wrapper.get_voyage_schedule(ssn, date)