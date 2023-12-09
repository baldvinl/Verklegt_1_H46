from data.aircraft_data import Aircraft_Data
from model.aircraft import Aircraft

class Aircraft_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_aircraft(self, aircraft):
        """Receives aircraft object and forwards to data wrapper"""
        return self.data_wrapper.register_aircraft(aircraft)

    def display_aircraft_info(self, name):
        """Receives aircraft name and forwards to data wrapper"""
        return self.data_wrapper.display_aircraft_info(name)

    def display_aircraft_status(self, name): # for later
        """Receives aircraft name and forwards to data wrapper"""
        return self.data_wrapper.display_aircraft_status(name)

    def display_all_aircrafts(self, date, time): # for later
        """Receives date and time and forwards to data wrapper"""
        return self.data_wrapper.display_aircraft_info(date, time)