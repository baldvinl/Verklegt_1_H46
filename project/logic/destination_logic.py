from data.data_wrapper import Data_Wrapper
from model.destination import Destination
from model.error_messages import ErrorMessages
from logic.validation_check import ValidationLogic

class Destination_Logic:
    def __init__(self, data_connection: Data_Wrapper, validation_instance: ValidationLogic):
        self.data_wrapper = data_connection
        self.validation_check = validation_instance

    def register_destination(self, new_destination: Destination):
        """Receives destination, checks if it already exists, if so gives error, if not it forwards
        the new destination to data wrapper."""
        self.validation_check.destination_already_in_system_check(new_destination)
        if new_destination.ice_name and new_destination.ice_number:
            return self.data_wrapper.register_destination_in_file(new_destination)

    def get_all_destinations(self):
        """Requests destinations list from data wrapper. If empty returns error otherwise returns list"""
        destinations_list = self.data_wrapper.get_destinations_from_file()
        if destinations_list:
            return destinations_list
        else:
            raise ValueError(ErrorMessages.DESTINATION_NOT_FOUND)
    
    def get_destination(self, airport: str):
        """Requests lists of all destinations from data wrapper. If destination is not found it returns an error
        if not it finds specific destination with airport provided and returns it."""
        destinations_list = self.get_all_destinations()
        for destination in destinations_list:
            if destination.airport == airport:
                return destination
        raise ValueError(ErrorMessages.DESTINATION_NOT_FOUND)

    def change_emergency_contact_info(self, airport: str, new_info: tuple):
        """Receives airport and new_info tuple with the format (new_name, new_number) - if one of those doesn't need to be changed
        it will be set to "None", requests destination object from data
        wrapper using airport, changes the information and returns updated destination object"""
        destination = self.get_destination(airport)
        if destination:
            if new_info[0]:
                destination.ice_name = new_info[0]
            if new_info[1]:
                destination.ice_number = new_info[1]
            return self.data_wrapper.register_updated_destination_to_file(destination)
        else:
            raise ValueError(ErrorMessages.DESTINATION_NOT_FOUND)