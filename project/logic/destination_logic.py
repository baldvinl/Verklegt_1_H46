from data.data_wrapper import data_wrapper
from model.destintion import destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        return self.data_wrapper.register_destination(destination)

    def display_destination(self, aita):
        return self.data_wrapper.display_destination(aita)

    def change_ice_name(self, name, aita):
        return self.data_wrapper.change_ice_name(name, aita)

    def change_ice_number(self, number, aita):
        return self.data_wrapper.change_ice_number(number, aita)