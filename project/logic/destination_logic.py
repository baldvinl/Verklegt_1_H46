from data.destination_data import Destination_Data
from model.destination import Destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination):
        """Receives destination object and forwards to data wrapper"""
        return self.data_wrapper.register_destination(destination)

    def display_destinations(self):
        """Forwards request to data wrapper"""
        return self.data_wrapper.display_destinations()

    def change_ice_info(self, iata, new_info):
        """Receives iata and new_info tuple, requests destination object from data
        wrapper using iata, changes the information and returns updated destination object"""
        # send iata and get destination object back from data
        destination = self.data_wrapper.get_destination_from_file(iata) 
        # new info is tuple [(name, number)]
        # change object here and send back to data
        if new_info[0]:
            destination.ice_name = new_info[0]
        if new_info[1]:
            destination.ice_number = new_info[1]
        return destination