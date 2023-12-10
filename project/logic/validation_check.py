from logic.aircraft_logic import Aircraft_Logic
from logic.crew_logic import Crew_Logic
from logic.destination_logic import Destination_Logic
from logic.voyage_logic import Voyage_Logic

# def find_crew_member(ssn, crew_list):
#     for crew_member in crew_list:
#         if crew_member.ssn == ssn:
#             return True
#         return False

class ValidationLogic:

    NOT_FOUND = "NF"
    ALREADY_IN_SYSTEM = "AIS"

    def __init__(self) -> None:
        pass

    # TODO
    # check if crew member is already registered - IN
    def find_crew_member(self, ssn_to_register: str, all_crew_list: list):
        """Checks if ssn has already been registered in the crew list"""
        for crew_member in all_crew_list:
            if crew_member.ssn == ssn_to_register:
                return True
            return False
    # in listing employee info - needs to be registered - IN
    # change info crew - need to exist - IN 
    # destination register - IN 
    #   needs to have ice contact/ needs to not exist yet - IN
    # change ice info - destination needs to exist - IN
    # register voyage - check if exists already/ if departure time from iceland is within 30 min from another voyage
    # add crew to voyage - voyage needs to exist/ aircraft has been added?/ 





    # Crew
        # Name [just letters 3-30 - no numbers or symbol] -- maybe split functions for first and last name
        # SSN [just digits up to 10]
        # Phone number [just digits up to 15]
        # Address [just numbers and letters, dashes, spaces]
        # Landline -- same as phone number probably 
        # Email first part cant contain ".", one "@" only, second part needs to contain "."

    def validate_name(self, name):
        pass

    def validate_ssn(self, ssn):
        pass

    def validate_phone_number(self, number):
        pass

    def validate_address(self, address):
        pass

    def validate_email(self, email):
        pass

    # Aircraft
        # Name [2 letters 3 numbers]
        # Type 
        # Manufacturer [probably use validate name?]
        # seat count 
        # status

    def validate_aircraft_name(self, name):
        pass

    # Destination
        # Country
        # Airport
        # Flight time
        # Flight duration
        # Distance from iceland
        # emergency contact name
        # number

    # Voyage
        # Destination
        # flight to
        # flight back
        # fully manned
        # status
        # pilot count
        # f.a count