# from project.logic.logic_wrapper import Logic_Wrapper
import re

PUNCTUATION_IN_STRING_ERROR_MESSAGE = 'There is punctuation in the string'
DIGIT_IN_STRING_ERROR_MESSAGE = 'There is a digit in the string'
LETTER_IN_STRING_ERROR_MESSAGE = 'There is a letter in the string'
MUST_BE_DIGITS_AND_CORRECT_LENGHT_ERROR_MESSAGE = 'There are non-digit characters in a string. The string is not correct lenght'
MUST_BE_LETTERS_AND_CORRECT_LENGHT_ERROR_MESSAGE = 'There are non-letter characters in the string. he string is not correct lenght'
PUNCTUATION_AND_CORRECT_LENGHT_ERROR_MESSAGE = 'There is punctuation in the string. The string is not the correct lenght.'
EMAIL_INCORRECT_ERROR_MESSAGE = 'The email has not correct format'
MUST_BE_CAPITAL_LETTERS_AND_CORRECT_LENGHT_ERROR_MESSAGE = 'There are non-capital-letter characters in the string.The string is not correct lenght'
INCORRECT_TIME_ERROR_MESSAGE = 'The time is not in correct format'
NOT_DIGIT_ERROR_MESSAGE = 'There are non-digit character in the string'
AIRCRAFT_NAME_ERROR_MESSAGE = 'Aircraft name is not in correct format (XX:XXX)'


class Validation_Ui:
    def __init__(
        self,
        punctuation,
        numbers,
        letters,
        ssn,
        name_country,
        phone,
        address,
        email,
        airport,
        flight_time,
        distance,
        aircraft_name
    ):
        self.symbols = punctuation
        self.numbers = numbers
        self.letters = letters
        self.ssn = ssn
        self.name_country = name_country
        self.phone = phone
        self.address = address
        self.email = email
        self.airport = airport
        self.flight_time = flight_time
        self.distance = distance
        self.aircraft_name = aircraft_name

    def validate_no_punctuation(self, punctuation):
        """Raise error when there are punctuation in a string"""

        validate = r"^[a-zA-Z0-9 ]+$"
        if not re.search(validate, punctuation):

            raise ValueError(DIGIT_IN_STRING_ERROR_MESSAGE)
        return punctuation

    def validate_no_numbers(self, numbers):
        """Raise error when there is a number in a string"""

        validate = r"\d"
        if re.search(validate, numbers):
            raise ValueError(DIGIT_IN_STRING_ERROR_MESSAGE)
        return numbers

    def validate_no_letter(self, letters):
        """Raise error when there is a letter in a string"""

        validate = r"[a-zA-Z]"
        if re.search(validate, letters):
            raise ValueError(LETTER_IN_STRING_ERROR_MESSAGE)
        return letters

    def validate_ssn(self, ssn):
        """Validate social security number. Raise error if ssn is not 10 digits"""

        validate = r"^\d{10}+$"
        if not re.search(validate, ssn):
            raise ValueError(MUST_BE_DIGITS_AND_CORRECT_LENGHT_ERROR_MESSAGE)
        return ssn

    def validate_name_and_country(self, name_country):
        """Validate names and countries. Raise error if string contains digits or
        punctuation and lenght is not between 2 - 15"""

        validate = r"^[a-zA-Z]{2,15}+$"
        if not re.search(validate, name_country):
            raise ValueError(PUNCTUATION_AND_CORRECT_LENGHT_ERROR_MESSAGE))
        return name_country

    def validate_phone_number(self, phone):
        """Validate phone number. Raise error if number is not digits
        between 7 - 15"""

        validate = r"^\d{7,15}+$"
        if not re.search(validate, phone):
            raise ValueError(MUST_BE_DIGITS_AND_CORRECT_LENGHT_ERROR_MESSAGE)
        return phone

    def validate_address(self, address):
        """Validate address. Raise error if address has punctuation in it and is
        not between 2 - 15 characters"""
        validate = r"^[a-zA-Z0-9 ]{2,15}+$"
        if not re.search(validate, address):
            raise ValueError(PUNCTUATION_AND_CORRECT_LENGHT_ERROR_MESSAGE)
        return address

    def validate_email(self, email):
        """Validate email. Raise error if email is not on with correct format.
        Email prefix can contain letter or digits with or without .-_
        After prefix is @
        Email domain has to have at least 1 dot in between letters
        ex. jane.rakel.smith@mail.co.uk"""
        valitity = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        if not re.search(valitity, email):
            print(EMAIL_INCORRECT_ERROR_MESSAGE)
            raise ValueError
        return email

    def validate_airport(self, airport):
        """Validate airport name. Raise error if name is not 3 capitalized letters"""

        validate = r"^[A-Z]{3}+$"
        if not re.search(validate, airport):
            print(MUST_BE_CAPITAL_LETTERS_AND_CORRECT_LENGHT_ERROR_MESSAGE)
            raise ValueError
        return airport

    def validate_flight_time(self, flight_time):
        '''Validate flight time. Raise error if time has not this format: 13:45'''
        validate = r"^[0-2][0-9][:][0-5][0-9]"

        if not re.search(validate, flight_time):
            print(INCORRECT_TIME_ERROR_MESSAGE)
            raise ValueError
        return flight_time

    def validate_distance(self, distance):
        '''Validate distance. Raise error if distance is not digits '''

        validate = r"^\d+$"
        if not re.search(validate, distance):
            print(NOT_DIGIT_ERROR_MESSAGE)
            raise ValueError
        return distance

    def validate_aircraft_name(self, aircraft_name):
        '''Validate aircraft name. Raise error format of the name is not "XX-XXX"
        Ex TF-FFR'''

        valitity = r"^[A-Z]{2}-[A-Z]{3}$"
        if not re.search(valitity, aircraft_name ):
            print(AIRCRAFT_NAME_ERROR_MESSAGE)
            raise ValueError
        return aircraft_name
