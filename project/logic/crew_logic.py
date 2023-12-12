from data.data_wrapper import Data_Wrapper
from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant
from model.error_messages import ErrorMessages

class Crew_Logic:
    def __init__(self, data_connection: Data_Wrapper, voyage_logic_instance):
        self.data_wrapper = data_connection
        self.voyage_logic = voyage_logic_instance

    def get_crew_member(self, ssn: str):
        """Receives social security number of crew member, checks if already exists and forwards to data wrapper
        if not it returns an error code"""
        all_crew = self.get_all_crew()
        for member in all_crew:
            if member.ssn == ssn:
                return member
        raise ValueError(ErrorMessages.NO_CREW_FOUND)

    def register_crew(self, crew: Crew):
        """Receives crew object, checks if member with same ssn already exists, if not checks 
        if crew object received is of the type Pilot or not and forwards to data wrapper accordingly"""
        crew_member = self.get_crew_member(crew.ssn)
        if not crew_member:
            if isinstance(crew, Pilot):
                return self.data_wrapper.register_pilot_to_file(crew)
            else:
                return self.data_wrapper.register_flight_attendant_to_file(crew)
        else:
            raise ValueError(ErrorMessages.CREW_MEMBER_ALREADY_IN_SYSTEM)
        
    def get_pilots(self):
        """Requests all pilots from data wrapper and returns if there is any. 
        If not returns error code"""
        pilots_list = self.data_wrapper.get_pilots_from_file()
        if pilots_list:
            return pilots_list
        else:
            raise ValueError(ErrorMessages.NO_PILOTS_FOUND)
        
    def get_flight_attendants(self):
        """Requests all flight attendants from data wrapper and returns if there is any. 
        If not returns error code"""
        flight_attendants_list = self.data_wrapper.get_flight_attendants_from_file()
        if flight_attendants_list:
            return flight_attendants_list
        else:
            raise ValueError(ErrorMessages.NO_FLIGHT_ATTENDANTS_FOUND)
    
    def get_all_crew(self):
        """Receives lists of pilots and flight attendants 
        from data wrapper, combines them and returns list if not empty, otherwise an error code"""
        pilots_list = self.data_wrapper.get_pilots_from_file()
        flight_attendants_list = self.data_wrapper.get_flight_attendants_from_file()
        all_crew_list = pilots_list + flight_attendants_list
        if all_crew_list:
            return all_crew_list
        else:
            raise ValueError(ErrorMessages.NO_CREW_FOUND)

    def change_crew_info(self, ssn: str, changes: list[tuple]):
        """Receives ssn, and changes list of tuples with format 
        [(attribute, new_value)], requests crew member with ssn
        changes attributes with their new values 
        and returns updated object to data wrapper"""
        crew_member = self.get_crew_member(ssn)
        if crew_member:
            for attribute_name, new_value in changes:
                attribute_name_lower = attribute_name.lower()
                setattr(crew_member, attribute_name_lower, new_value)
            if isinstance(crew_member, Pilot):
                return self.data_wrapper.register_updated_pilot_to_file(crew_member)
            else:
                return self.data_wrapper.register_updated_flight_attendant_to_file(crew_member)
        else:
            raise ValueError(ErrorMessages.NO_CREW_FOUND)

    def crew_status(self, departure_time, busy: bool):
        """Receives departure time and availability request (working or not working), requests
        voyages that day using the date from data wrapper, gets all crew from data wrapper. Using
        the ssns found in the voyages that day it makes 2 lists one for crew thats working
        and one for crew that isnt. Then returns according to the availability requested"""

        voyages_that_day = self.voyage_logic.get_voyages_day(departure_time)
        crew = self.get_all_crew()
        attributes_list = ["pilot", "captain", "head_flight_attendant", "extra_flight_attendants"]

        if not voyages_that_day: #TODO
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)
        
        ssn_list = []
        for attribute in attributes_list:
            attribute_value = getattr(voyages_that_day, attribute)
            ssn_list.append(attribute_value)
        if not crew:
            raise ValueError(ErrorMessages.NO_CREW_FOUND)
        
        crew_not_working = []
        crew_working = []
        for crew_member in crew:
            if crew_member.ssn not in ssn_list:
                crew_not_working.append(crew_member)
            else:
                crew_working.append(crew_member, voyages_that_day.destination)
                
        if not busy:
            return crew_not_working
        return crew_working
    
    def find_crew_for_voyage(self, departure_time):
        """Receives date, requests crew not working on that date, returns dictionary with key: job title 
        and fills with all crew members separated by their job title, if there is no crew it returns
        error code"""
        busy = False
        job_title = ["captain", "pilot", "head flight attendant", "extra flight attendants"]
        crew_not_working = self.crew_status(departure_time, busy)
        if crew_not_working:
            crew_dict = dict.fromkeys(job_title, None)
            for member in crew_not_working:
                if member.job_title in crew_dict:
                    crew_dict[member.job_title].append(member)
            return crew_dict
        else:
            raise ValueError(ErrorMessages.NO_CREW_FOUND)