# from project.logic.logic_wrapper import Logic_Wrapper

ERROR_MESSAGE = "An error occured. The program will shut down"
INCORRECT_INPUT = 'Incorrect input'
CORRECT_FORMAT = "This is a correct input"
SSN_LEN = 10
NAME_LEN_MINIMUM = 3
NAME_LEN_MAXIMUM = 30
MOBILE_LEN_MINIMUM = 7
MOLBILE_LEN_MAXIMUM = 15

# ------------CREW---------------------


class Validation_Ui:
    def __init__(self, ssn, name, mobile, address):
        self.ssn = ssn
        self.name = name
        self.mobile = mobile
        self.address = address
        return None

    def validate_ssn(self, ssn):
        while True:
            try:
                if len(ssn) == SSN_LEN and any(char.isdigit() for char in ssn):
                    # return address
                    # Logic_Wrapper...
                    break
                else:
                    print(INCORRECT_INPUT)
                    print("SSN should have 10 digits")
                    ssn = input("Enter a correct SSN: ")
            except ValueError:
                print(ERROR_MESSAGE)
                break

    def validate_name(self, name):
        while True:
            try:
                if NAME_LEN_MINIMUM < len(name) <= NAME_LEN_MAXIMUM:
                    print('ok')
                    first_name, last_name = name.strip().split()
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
            # Mobile number [just digits up to 15]
            while not MOBILE_LEN_MINIMUM >= len(mobile) >= MOLBILE_LEN_MAXIMUM:
                for char in mobile:
                    if char.isdigit():
                        print(CORRECT_FORMAT)
                        # Logic_Wrapper.register_crew(mobile)
                    else:
                        print("This is not correct format.")
                        print("SSN has no digits")
                        mobile = input(
                            "Enter correct ssn: "
                        )  # sHOULD i put something else
                print("This is not valid format. SSN has 10 numbers")
                mobile = input("Enter correct ssn: ")

        def validate_address(self, address):
            # Address [just numbers and letters, dashes, spaces]
            string_punc = "!\"#$%&'()*+, ./:;<=>?@[\]^_`{|}~"
            while True:
                for char in address:
                    if char in string_punc:
                        print("This is not a valid address")
                        print("")
                        address = input("Enter correct address: ")
                    else:
                        print(CORRECT_FORMAT)
                        # return address
                        # Logic_Wrapper...
                        break

        def validate_home_phone_number(self, mobile):
            # Landline -- same as phone number probably
            while not MOBILE_LEN_MINIMUM >= len(self.mobile) >= MOLBILE_LEN_MAXIMUM:
                for char in self.mobile:
                    if char.isdigit():
                        print(CORRECT_FORMAT)
                        # Logic_Wrapper.register_crew(mobile)
                    else:
                        print("This is not correct format.")
                        print("SSN has no digits")
                        self.mobile = input(
                            "Enter correct ssn: "
                        )  # sHOULD i put something else
                print(
                    "This is not valid format. Number should be between 7 and 15 numbers"
                )
                self.mobile = input("Enter correct ssn: ")

        # Email first part cant contain ".", one "@" only, second part needs to contain "."

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
