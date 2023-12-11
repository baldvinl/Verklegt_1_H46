from data.data_wrapper import Data_Wrapper
from model.destination import Destination
from logic.validation_check import ValidationLogic

class Destination_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection

    def register_destination(self, destination: Destination):
        """Receives destination object and forwards to data wrapper""" #TODO
        destination = self.get_destination(destination.airport)
        if not destination & destination.ice_name & destination.ice_number:
            return self.data_wrapper.register_destination(destination)
        else:
            return ValidationLogic.ALREADY_IN_SYSTEM

    def get_all_destinations(self):
        """Forwards request to data wrapper""" #TODO
        return self.data_wrapper.get_destinations_from_file()
    
    def get_destination(self, iata: str):
        """ todo"""
        destinations_list = self.get_all_destinations()
        for destination in destinations_list:
            if destination.airport == iata:
                return destination

    def change_ice_info(self, iata: str, new_info: list):
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