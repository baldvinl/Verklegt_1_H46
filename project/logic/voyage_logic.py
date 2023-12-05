from data.data_wrapper import data_wrapper
from model.voyage import Voyage

class Voyage_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_voyage(self, voyage):
        pass

        self.data_wrapper.register_voyage(voyage)

    def get_crew_info(self, ):
        pass

        self.data_wrapper.get_information()

    def add_crew(self, crew, voyage):
        pass

        self.data_wrapper.add_crew()

    def display_voyage(self):
        pass

    def get_voyage_status(self):
        pass

    def display_all_voyages_day(self, day):
        pass

    def display_all_voyages_week(self, week):
        pass

    def get_voyage_schedule(self, crew, day):
        pass