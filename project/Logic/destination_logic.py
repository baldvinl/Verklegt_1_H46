from data.data_wrapper import data_wrapper
from model.destintion import Destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        pass

    def display_destination(self):
        pass

    def change_ice_name(self, ):
        pass

        self.data_wrapper.change_ice_name() # why is this outside the function??

    def change_ice_number(self, ):
        pass

        self.data_wrapper.change_ice_number()