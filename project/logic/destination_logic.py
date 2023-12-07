from data.data_wrapper import Data_Wrapper
from model.destination import Destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        return self.data_wrapper.register_destination(destination)

    def display_destination(self, iata):
        return self.data_wrapper.display_destination(iata)

    def change_ice_name(self, iata, name):
        return self.data_wrapper.change_ice_name(iata, name)

    def change_ice_number(self, iata, number):
        return self.data_wrapper.change_ice_number(iata, number)