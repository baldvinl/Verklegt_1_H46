from data.data_wrapper import data_wrapper
from model.destination import destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        return self.data_wrapper.register_destination(destination)

    def display_destination(self, aita):
        return self.data_wrapper.display_destination(aita)

    def change_ice_name(self, aita, name):
        return self.data_wrapper.change_ice_name(aita, name)

    def change_ice_number(self, aita, number):
        return self.data_wrapper.change_ice_number(aita, number)