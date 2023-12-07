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

    def display_voyage(self, destination, date):
        return self.data_wrapper.display_voyage(destination, date)

    def get_voyage_status(self,destination, date):
        return self.data_wrapper.get_voyage_status(destination, date)

    def display_all_voyages_day(self, day):
        return self.data_wrapper.display_all_voyages_day(day)

    def display_all_voyages_week(self, week):
        return self.data_wrapper.display_all_voyages_day(week)

    def get_voyage_schedule(self, crew, day):
        return self.data_wrapper.get_voyage_schedule(crew, day)