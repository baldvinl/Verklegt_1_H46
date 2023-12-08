
class Validation:
    def __init__(self) -> None:
        pass

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