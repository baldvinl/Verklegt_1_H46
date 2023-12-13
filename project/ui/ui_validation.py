# from project.logic.logic_wrapper import Logic_Wrapper
import re

SSN_LEN = 10
NAME_COUNTRY_LEN_MINIMUM = 2
NAME_COUNTRY_LEN_MAXIMUM = 15
phone_LEN_MINIMUM = 7
phone_LEN_MAXIMUM = 15
AIRCRAFT_NAME_LEN = 6
DASH = "-"
AIRCRAFT_NAME_FIRST_PART_LEN = 2
AIRCRAFT_NAME_LAST_PART_LEN = 3
AIRCRAFT_NAME_FIRST_ALPHA = ""
AIRCRAFT_NAME_LAST_ALPHA = ""
AIRCRAFT_NAME_VALUE_ERROR_MESSAGE = "The format is not correct"
AIRCRAFT_NAME_INPUT = "Enter a correct aircraft name:"
AIRPORT_NAME_LEN = 3
TIME_LEN = 5


# ------------CREW---------------------
class Validation_Ui:
    def __init__(self, punctuation, numbers, letters, ssn, name_country, phone, address, email):
        self.symbols = punctuation
        self.numbers = numbers
        self.letters = letters
        self.ssn = ssn
        self.name_country = name_country
        self.phone = phone
        self.address = address
        self.email = email
        # self.airport = airport
        # self.flight_time = flight_time
        # self.distance = distance

    def validate_no_punctuation(self, punctuation):
        validate = r"^[a-zA-Z0-9 ]+$"
        if not re.match(validate, punctuation):
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return punctuation

    def validate_no_numbers(self, numbers):
        #something wrong
        validate = r"^\d+$"
        if re.match(validate, numbers):
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return numbers
    
    def validate_no_letter(self, letters):
        #incorrect
        validate = r"^\d+$"
        if re.match(validate, letters):
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return letters

    def validate_ssn(self, ssn):
        """Validate social security number"""
        validate = r"^\d+$"
        if not re.match(validate, ssn) or len(ssn) != SSN_LEN:
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return ssn

    def validate_name_and_country(self, name_country):
        """Validate names and countries"""
        validate = r"^[a-zA-Z]+$"
        if (
            not re.match(validate, name_country)
            or len(name_country) < NAME_COUNTRY_LEN_MINIMUM
            or len(name_country) > NAME_COUNTRY_LEN_MAXIMUM
        ):
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return name_country

    def validate_phone_number(self, phone):
        """Validate phone number."""

        validate = r"^\d{7,15}+$"
        if not re.match(validate,phone):
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return phone

    def validate_address(self, address):
        """Validate crews address"""
        validate = r"^[a-zA-Z0-9 ]{2,15}+$"
        if not re.match(validate, address):
            raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
        return address

    def validate_email(self, email):
        valitity = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        if not re.search(valitity, email):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return email

    def validate_airport(self, airport):
        validate = r"^[A-Z]+$"
        if not re.match(validate, airport) or len(airport) != AIRPORT_NAME_LEN:
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return airport

    def validate_flight_time(self, flight_time):
        validate = r"^[0-2][0-9][:][0-5][0-9]"

        if not re.match(validate, flight_time):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return flight_time

    def validate_distance_from_iceland(self, distance):
        validate = r"^\d+$"
        if not re.match(validate, distance):
            print(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
            raise ValueError
        return distance


class Voyage_Validation:
    def __init__(
        self,
        destionation,
        flight_to,
        flight_from,
        fully_manned,
        status,
        pilot_count,
        f_a_count,
    ):
        self.destionation = destionation
        self.flight_to = flight_to
        self.flight_from = flight_from
        self.fully_manned = fully_manned
        self.status = status
        self.pilot_count = pilot_count
        self.f_a_count = f_a_count

    # flight to --> lfight number -wait
    # flight back --> validate alph
    # status --> what to validate n- wiat
    # pilot count --> validate int - wait
    # f.a count --> validate int -wait

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
