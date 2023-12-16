from data.data_wrapper import Data_Wrapper
from model.crew import Crew
from model.pilot import Pilot
from logic.voyage_logic import Voyage_Logic

class Crew_Logic:
    def __init__(self, data_connection: Data_Wrapper, voyage_logic_instance: Voyage_Logic):
        self.data_wrapper = data_connection
        self.voyage_logic = voyage_logic_instance

    def get_crew_member(self, ssn: str):
        """Receives social security number of crew member, checks if already exists and forwards to data wrapper
        if not it returns an error code"""
        all_crew_list = self.get_all_crew()
        if all_crew_list:
            for member in all_crew_list:
                if member.ssn == ssn:
                    return member
        
        return False

    def register_crew(self, crew):
        """Receives crew object, checks if member with same ssn already exists, if not checks 
        if crew object received is of the type Pilot or not and forwards to data wrapper accordingly"""
        already_exists = self.get_crew_member(crew.ssn)
        if not already_exists:
            if isinstance(crew, Pilot):
                return self.data_wrapper.register_pilot_to_file(crew)
            else:
                return self.data_wrapper.register_flight_attendant_to_file(crew)

    def get_pilots(self):
        """Requests all pilots from data wrapper and returns if there is any. 
        If not returns error code"""
        pilots_list = self.data_wrapper.get_pilots_from_file()
        if pilots_list:
            return pilots_list
        else:
                return False
        
    def get_flight_attendants(self):
        """Requests all flight attendants from data wrapper and returns if there is any. 
        If not returns error code"""
        flight_attendants_list = self.data_wrapper.get_flight_attendants_from_file()
        if flight_attendants_list:
            return flight_attendants_list
        else:
                return False
    
    def get_all_crew(self):
        """Receives lists of pilots and flight attendants from data wrapper, 
        combines them and returns list if not empty, otherwise an error code""" 
        pilots_list = self.data_wrapper.get_pilots_from_file()
        flight_attendants_list = self.data_wrapper.get_flight_attendants_from_file()
        all_crew_list = pilots_list + flight_attendants_list
        if all_crew_list:
            return all_crew_list
        else:
            return False

    def change_crew_info(self, crew_member):
        """Receives ssn, and changes list of tuples with format 
        [(attribute, new_value)], requests crew member with ssn
        changes attributes with their new values 
        and returns updated object to data wrapper"""
        
        # if it is an update we have missing job_title
        if crew_member.job_title == None:
            # try to get the person by the ssn
            original_entry = self.get_crew_member(crew_member.ssn)
            if original_entry == None:
                return False
            else:
                #we have a winner, so update his info parts
                original_entry.address = crew_member.address
                original_entry.email = crew_member.email
                original_entry.mobile_no = crew_member.mobile_no
                original_entry.phone_no = crew_member.phone_no
                # so we updated org with changes so now overwrite what we got
                crew_member = original_entry
        
        if isinstance(crew_member, Pilot):
            return self.data_wrapper.register_updated_pilot_to_file(crew_member)
        else:
            return self.data_wrapper.register_updated_flight_attendant_to_file(crew_member)
    
    def find_crew_for_voyage(self, departure_time):
        """Receives date, requests crew not working on that date, returns dictionary with key: job title 
        and fills with all crew members separated by their job title, if there is no crew it returns
        error code"""
        busy = False
        job_title = ["captain", "pilot", "head_flight_attendant"]
        crew_not_working = self.crew_status(departure_time, busy)
        if crew_not_working:
            crew_dict = dict.fromkeys(job_title, None)
            crew_dict.update({"flight_attendants": None})
            for member in crew_not_working:
                if member.job_title in job_title:
                    crew_dict[member.job_title].append(member)
                else:
                    crew_dict["flight_attendants"].append(member) #doesnt work 
            return crew_dict

    def crew_status(self, departure_time, busy: bool): #TODO
        """Receives departure time and availability request (working or not working), requests
        voyages that day using the date from data wrapper, gets all crew from data wrapper. Using
        the ssns found in the voyages that day it makes 2 lists one for crew thats working
        and one for crew that isnt. Then returns according to the availability requested"""

        voyages_that_day = self.voyage_logic.get_voyages_for_period(departure_time , 1)
        crew = self.get_all_crew()
        attributes_list = ["pilot", "captain", "head_flight_attendant", "flight_attendant1", "flight_attendant2"]

        # if not voyages_that_day:
        #     raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)
        
        ssn_list_of_crew_on_voyage = []
        for attribute in attributes_list:
            for voyage in voyages_that_day:
                attribute_value = getattr(voyage, attribute)
                ssn_list_of_crew_on_voyage.append(attribute_value)
        # if not crew:
        #     raise ValueError(ErrorMessages.NO_CREW_FOUND)
        
        crew_not_working = []
        crew_working = []
        for crew_member in crew:
            if crew_member.ssn not in ssn_list_of_crew_on_voyage:
                crew_not_working.append(crew_member)
            else:
                crew_working.append(crew_member, voyages_that_day.destination)
                
        if not busy:
            return crew_not_working
        return crew_working