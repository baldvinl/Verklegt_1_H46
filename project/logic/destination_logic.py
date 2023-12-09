from data.data_wrapper import Data_Wrapper
from model.destination import Destination

class Destination_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        """Receives destination object and forwards to data wrapper"""
        return self.data_wrapper.register_destination(destination)

    def display_destinations(self):
        """Forwards request to data wrapper"""
        return self.data_wrapper.display_destinations()

    def change_ice_info(self, iata, new_info):
        """Receives iata and new_info tuple with the format (new_name, new_number) - if one of those doesn't need to be changed
        it will be set to "None", requests destination object from data
        wrapper using iata, changes the information and returns updated destination object"""
        # send iata and get destination object back from data
        destination = self.data_wrapper.get_destination_from_file(iata) 
        # new info is tuple [(name, number)]
        # change object here and send back to data
        if new_info[0]:
            destination.ice_name = new_info[0]
        if new_info[1]:
            destination.ice_number = new_info[1]
        return self.data_wrapper.register_updated_destination_to_file(destination)