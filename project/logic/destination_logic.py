from data.data_wrapper import data_wrapper
from model.destintion import destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        return self.data_wrapper.register_destination(destination)

    def display_destination(self):
        return self.data_wrapper.display_destination 

    def change_ice_name(self, name):
        return self.data_wrapper.change_ice_name(name)

    def change_ice_number(self, number):
        return self.data_wrapper.change_ice_number(number)