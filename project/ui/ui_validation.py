# from project.logic.logic_wrapper import Logic_Wrapper

ERROR_MESSAGE = "An error occured. The program will shut down"
INCORRECT_INPUT = "Incorrect input"
CORRECT_FORMAT = "This is a correct input"
SSN_LEN = 10
NAME_LEN_MINIMUM = 3
NAME_LEN_MAXIMUM = 30
MOBILE_LEN_MINIMUM = 7
MOBILE_LEN_MAXIMUM = 15
AIRCRAFT_NAME_LEN = 6
DASH = '-'
AIRCRAFT_NAME_FIRST_PART_LEN = 2
AIRCRAFT_NAME_LAST_PART_LEN = 3
AIRCRAFT_NAME_FIRST_ALPHA = ''
AIRCRAFT_NAME_LAST_ALPHA = ''
AIRCRAFT_NAME_VALUE_ERROR_MESSAGE = 'Name is in this format: XX-XXX'
AIRCRAFT_NAME_INPUT = 'Enter a correct aircraft name:'

# ------------CREW---------------------
class Validation_Ui:
    def __init__(self, ssn, crew_name, mobile, address):
        self.ssn = ssn
        self.crew_name = crew_name
        self.mobile = mobile
        self.address = address
        return None

    def validate_ssn(self, ssn):
        while True:
            try:
                if len(ssn) == SSN_LEN and any(char.isdigit() for char in ssn):
                    return False 
                else:
                    print(INCORRECT_INPUT)
                    print("SSN should have 10 digits")
                    ssn = input("Enter a correct SSN: ")
            except ValueError:
                print(ERROR_MESSAGE)
                break

    def validate_name(self, crew_name):
        while True:
            try:
                if NAME_LEN_MINIMUM < len(crew_name) <= NAME_LEN_MAXIMUM:
                    print("ok")
                    first_name, last_name = crew_name.strip().split()
                    return (first_name, last_name)
                    # break
                    # Logic_Wrapper.register_crew(first_name, last_name)
                else:
                    print(INCORRECT_INPUT)
                    print("Input name lenght should be between 3 and 30 charachter")
                    name = input("Enter a name with correct lenght: ")
            except ValueError:
                print(ERROR_MESSAGE)
                break

    def validate_mobile_number(self, mobile):
        # Mobile number [just digits up to 15].
        #something is wrong with this code
        while True:

            try:
                if MOBILE_LEN_MINIMUM < len(mobile) < MOBILE_LEN_MAXIMUM and any(
                    char.isdigit() for char in mobile
                ):
                    # return address
                    # Logic_Wrapper...
                    break
                else:
                    print(INCORRECT_INPUT)
                    print("Mobile number should be digits between 7 and 15")
                    mobile = input("Enter a correct mobile: ")
            except ValueError:
                print(ERROR_MESSAGE)
                break

    def validate_address(self, address):
        # Address [just numbers and letters, dashes, spaces]
        string_punc = "!\"#$%&'()*+, ./:;<=>?@[\]^_`{|}~"
        while True:
            try:
                if not any(char in string_punc for char in address):
                    # return address
                    # Logic_Wrapper...
                    break
                else:
                    print(INCORRECT_INPUT)
                    print("The address is in a wrong format...and something more")
                    address = input("Enter a correct address: ")
            except ValueError:
                print(ERROR_MESSAGE)
                break

    def validate_home_phone_number(self, home_phone):
        # Landline -- same as phone number probably
        # Mobile number [just digits up to 15].
        #something is wrong with this code
        while True:
            try:
                if MOBILE_LEN_MINIMUM < len(home_phone) < MOBILE_LEN_MAXIMUM and any(
                    char.isdigit() for char in home_phone
                ):
                    # return address
                    # Logic_Wrapper...
                    break
                else:
                    print(INCORRECT_INPUT)
                    print("Mobile number should be digits between 7 and 15")
                    home_phone = input("Enter a correct mobile: ")
            except ValueError:
                print(ERROR_MESSAGE)
                break

        # Email first part cant contain ".", one "@" only, second part needs to contain "."

    def validate_email(self, email):
        pass


class Validate_Aircraft_Ui:
    def __init__(self, aircraft_name, aircraft_type, manufacturer, seat_count):
        self.aircraft_name = aircraft_name
        self.aircraft_type = aircraft_type
        self.manufacturer = manufacturer
        self.seat_count = seat_count
        return None

    def validate_aircraft_name(self, aircraft_name):
        while True:
            if not AIRCRAFT_NAME_LEN == len(aircraft_name):
                raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
                aircraft_name = input("Enter a correct aircraft name: ")   
            if not AIRCRAFT_NAME_FIRST_PART_LEN == len(aircraft_name[0:1]): 
                raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
                aircraft_name = input("Enter a correct aircraft name: ")
            if not AIRCRAFT_NAME_LAST_PART_LEN == len(aircraft_name[3:5]):
                raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
                aircraft_name = input("Enter a correct aircraft name: ")
            if not AIRCRAFT_NAME_FIRST_ALPHA.isalpha():
                raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
                aircraft_name = input("Enter a correct aircraft name: ")
            if not AIRCRAFT_NAME_LAST_ALPHA.isalpha():
                raise ValueError(AIRCRAFT_NAME_VALUE_ERROR_MESSAGE)
                aircraft_name = input("Enter a correct aircraft name: ")
            else:
                return False


    # Aircraft
    # Name [2 letters 3 numbers]
    # Type
    # Manufacturer [probably use validate name?]
    # seat count


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
