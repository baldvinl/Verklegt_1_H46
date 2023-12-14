from data.data_wrapper import Data_Wrapper
from model.error_messages import ErrorMessages
from model.destination import Destination
from model.crew import Crew

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

    # VALIDATION FUNCTIONS

    def destination_already_in_system_check(self, new_destination: Destination):
        all_destination = self.data_wrapper.get_destinations_from_file()
        for destination in all_destination:
            if destination.airport == new_destination.airport:
                raise ValueError(ErrorMessages.DESTINATION_ALREADY_IN_SYSTEM)

    def crew_already_in_system_check(self, new_member: Crew):
        all_crew = self.get_all_crew()
        for crew_member in all_crew:
            if crew_member.ssn == new_member.ssn:
                raise ValueError(ErrorMessages.CREW_MEMBER_ALREADY_IN_SYSTEM)
            
    def crew_not_in_system_check(self, ssn):
        all_crew = self.get_all_crew()
        ssn_list = []
        if all_crew:
            for crew_member in all_crew:
                ssn_list.append(crew_member.ssn)
            if ssn not in ssn_list:
                raise ValueError(ErrorMessages.NO_CREW_FOUND)
            
    def pilots_in_file_check(self):
        pass

    def flight_attendants_in_file_check(self):
        pass

    def crew_in_file_check(self):
        pass

    # UTILITY FUNCTIONS

    def get_all_crew(self):
        """Requests crew lists from data wrapper and combines them in one to get all crew"""
        all_pilots = self.data_wrapper.get_pilots_from_file()
        all_flight_attendants = self.data_wrapper.get_flight_attendants_from_file()
        all_crew = all_pilots + all_flight_attendants
        return all_crew
    
    def get_all_crew_ssn(self):
        """Requests crew lists, and makes a list of all the social security numbers"""
        all_crew = self.get_all_crew()
        ssn_list = []
        if all_crew:
            for crew_member in all_crew:
                ssn_list.append(crew_member.ssn)
            return ssn_list