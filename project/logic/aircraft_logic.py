from data.data_wrapper import Data_Wrapper
from model.aircraft import Aircraft

class Aircraft_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection

    def register_aircraft(self, aircraft: Aircraft):
        """Receives aircraft object and forwards to data wrapper"""
        return self.data_wrapper.register_aircraft(aircraft)

    def get_aircraft_info(self, name: str):
        """Receives aircraft name and forwards to data wrapper"""
        return self.data_wrapper.get_aircraft_info(name)

    def get_aircraft_status(self, name: str): # for later
        """Receives aircraft name and forwards to data wrapper"""
        return self.data_wrapper.get_aircraft_status(name)

    def get_all_aircrafts(self, datetime): # for later
        """Receives datetime, requests aicrafts from data and returns the list"""
        aicrafts_list = self.data_wrapper.get_aircraft_info(datetime)
        return aicrafts_list