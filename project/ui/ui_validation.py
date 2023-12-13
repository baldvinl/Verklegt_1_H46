# from project.logic.logic_wrapper import Logic_Wrapper
import re

SSN_LEN = 10
NAME_LEN_MINIMUM = 3
NAME_LEN_MAXIMUM = 30
MOBILE_LEN_MINIMUM = 7
MOBILE_LEN_MAXIMUM = 15
AIRCRAFT_NAME_LEN = 6
DASH = "-"
AIRCRAFT_NAME_FIRST_PART_LEN = 2
AIRCRAFT_NAME_LAST_PART_LEN = 3
AIRCRAFT_NAME_FIRST_ALPHA = ""
AIRCRAFT_NAME_LAST_ALPHA = ""
AIRCRAFT_NAME_VALUE_ERROR_MESSAGE = "Name is in this format: XX-XXX"
AIRCRAFT_NAME_INPUT = "Enter a correct aircraft name:"
COUNTRY_LEN_MIN = 2
COUNTRY_LEN_MAX = 30
IATA_LEN = 3
TIME_LEN = 5



# ------------CREW---------------------
class Crew_Validation_Ui:
    def __init__(self, ssn, crew_name, mobile, address, email):
        self.ssn = ssn
        self.crew_name = crew_name
        self.mobile = mobile
        self.address = address
        self.email = email
        return None

    def validate_ssn(self, ssn):
        # skoða
        validity = r"^\d+$"
        if not re.match(validity, ssn) or len(ssn) != SSN_LEN:
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return ssn

    def validate_name(self, crew_name):
        if len(crew_name) < NAME_LEN_MINIMUM or len(crew_name) > NAME_LEN_MAXIMUM:
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return crew_name

    def validate_mobile_number(self, mobile):
        '''Validate mobile number.'''
        validity = r"^\d+$"
        if (
            len(mobile) < MOBILE_LEN_MINIMUM
            or len(mobile) > MOBILE_LEN_MAXIMUM
            or not re.match(validity, mobile)):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return mobile

    def validate_address(self, address):
        """Validate crews address"""
        string_punc = r"[^!\"#$%&'()*+,/:;<=>?@[]_`{|}~]"

        if any(char in string_punc for char in address):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return address

    def validate_home_phone_number(self, home_phone):
        '''Validate mobile number.'''
        validity = r"^\d+$"
        if (
            len(home_phone) < MOBILE_LEN_MINIMUM
            or len(home_phone) > MOBILE_LEN_MAXIMUM
            or not re.match(validity, home_phone)):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return home_phone

    def validate_email(self, email):
        valitity = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if not re.search(valitity, email):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return email

class Destination_Ui_Validation:
    def __init__(self, country, airport, flight_time, flight_duration, distance, ice_name, ice_number):
        self.country = country
        self.airport = airport
        self.flight_time = flight_time
        self.flight_duration = flight_duration
        self.distance = distance
        self.ice_name = ice_name
        self.ice_number = ice_number

    def validate_country(self,country):
        if len(country) < COUNTRY_LEN_MIN or len(country) > COUNTRY_LEN_MAX:
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return country
    
    def validate_airport(self, airport):
        validity = r'^[A-Z]+$'
        if not re.match(validity,airport ) or len(airport) != IATA_LEN:
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return airport
    
    def validate_flight_time(self, flight_time):
        validity = r'^[0-2][0-9][:][0-5][0-9]'

        if not re.match(validity,flight_time):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return flight_time

    def validate_duration(self, flight_duration):
        validity = r'^[0-2][0-9][:][0-5][0-9]'
    
        if not re.match(validity,flight_duration):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return flight_duration
    

    def validate_distance_from_iceland(self, distance):
        validity = r"^\d+$"
        if not re.match(validity, distance):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return distance
    
    def validate_ice_number(self, ice_number):
        validity = r"^\d+$"
        if (
            len(ice_number) < MOBILE_LEN_MINIMUM
            or len(ice_number) > MOBILE_LEN_MAXIMUM
            or not re.match(validity, ice_number)):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return ice_number
    

class Voyage_Validation:
    def __init__(self, destionation, flight_to, flight_from, fully_manned, status, pilot_count, f_a_count):
        self.destionation = destionation
        self.flight_to = flight_to
        self.flight_from = flight_from
        self.fully_manned = fully_manned
        self.status = status
        self.pilot_count = pilot_count
        self.f_a_count = f_a_count

    def validate_destination(self, voyage):
        validity = r"^[a-zA-Z]+$"
        if not re.match(validity, voyage):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return voyage


# flight to --> validate alpha
# flight back --> validate alph
# fully manned  --> validate yes or no
# status --> what to validate
# pilot count --> validate int
# f.a count --> validate int


class Validate_Aircraft_Ui:
    def __init__(self, aircraft_name, aircraft_type, manufacturer, seat_count):
        self.aircraft_name = aircraft_name
        self.aircraft_type = aircraft_type
        self.manufacturer = manufacturer
        self.seat_count = seat_count
        return None

    def validate_aircraft_name(self, aircraft_name):
        valitity = "([A-Za-z]+[-]+([A-Z|a-z])"

        if not AIRCRAFT_NAME_LEN == len(aircraft_name) and re.match(
            valitity, aircraft_name
        ):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return aircraft_name

    # Name [2 letters 3 numbers]
    # Type
    # Manufacturer [probably use validate name?]
    # seat count
