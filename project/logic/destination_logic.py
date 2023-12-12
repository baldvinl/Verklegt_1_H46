from data.data_wrapper import Data_Wrapper
from model.destination import Destination
from logic.validation_check import ValidationLogic

class Destination_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection

    def register_destination(self, new_destination: Destination):
        """Receives destination, checks if it already exists, if so gives error, if not it forwards
        the new destination to data wrapper.""" 
        destination_check = self.get_destination(new_destination.airport)
        if not destination_check:
            if new_destination.ice_name & new_destination.ice_number:
                return self.data_wrapper.register_destination_in_file(new_destination)
        else:
            return ValidationLogic.ALREADY_IN_SYSTEM

    def get_all_destinations(self):
        """Requests destinations list from data wrapper. If empty returns error otherwise returns list"""
        destinations_list = self.data_wrapper.get_destinations_from_file()
        if destinations_list:
            return destinations_list
        else:
            return ValidationLogic.DESTINATION_NOT_FOUND
    
    def get_destination(self, iata: str):
        """Requests lists of all destinations from data wrapper. If destination is not found it returns an error
        if not it finds specific destination with iata provided and returns it."""
        destinations_list = self.get_all_destinations()
        for destination in destinations_list:
            if destination.airport == iata:
                return destination
        return ValidationLogic.DESTINATION_NOT_FOUND

    def change_ice_info(self, iata: str, new_info: tuple):
        """Receives iata and new_info tuple with the format (new_name, new_number) - if one of those doesn't need to be changed
        it will be set to "None", requests destination object from data
        wrapper using iata, changes the information and returns updated destination object"""
        # send iata and get destination object back from data
        destination = self.get_destination(iata)
        # new info is tuple [(name, number)]
        # change object here and send back to data
        if destination:
            if new_info[0]:
                destination.ice_name = new_info[0]
            if new_info[1]:
                destination.ice_number = new_info[1]
            return self.data_wrapper.register_updated_destination_to_file(destination)
        else:
            return ValidationLogic.NOT_FOUND