from logic.aircraft_logic import Aircraft_Logic
from logic.crew_logic import Crew_Logic
from logic.destination_logic import Destination_Logic
from logic.voyage_logic import Voyage_Logic

class ValidationLogic:
    def __init__(self) -> None:
        pass

    #TODO
    # check if crew member is already registered
    # in listing employee info - needs to be registered
    # change info crew - need to exist
    # destination register - needs to have ice contact/ needs to not exist yet
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