from data.data_wrapper import Data_Wrapper
from model.error_messages import ErrorMessages
from model.destination import Destination

class ValidationLogic:

    NOT_FOUND = "NF"
    ALREADY_IN_SYSTEM = "AIS"
    NO_VOYAGES_FOUND = "NVF"
    NO_CREW_FOUND = "NCF"
    DESTINATION_NOT_FOUND = "DNF"
    NO_PILOTS_FOUND = "NPF"
    NO_FLIGHT_ATTENDANTS_FOUND = "NFAF"

    def __init__(self, data_connection: Data_Wrapper) -> None:
        self.data_wrapper = data_connection

    def destination_already_in_system_check(self, new_destination: Destination):
        all_destination = self.data_wrapper.get_destinations_from_file()
        for destination in all_destination:
            if destination.airport == new_destination.airport:
                raise ValueError(ErrorMessages.DESTINATION_ALREADY_IN_SYSTEM)