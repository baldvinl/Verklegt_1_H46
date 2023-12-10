# from logic.logic_wrapper import Logic_Wrapper

CORRECT_FORMAT = 'This is a correct input'
SSN_LEN = 10
NAME_LEN_MINIMUM = 3
NAME_LEN_MAXIMUM = 30
MOBILE_LEN_MINIMUM = 7
MOLBILE_LEN_MAXIMUM = 15

# ------------CREW---------------------

class Validation_Ui:
    def __init__(self, ssn ,name, mobile, address):
        self.ssn = ssn
        self.name = name
        self.mobile = mobile
        self.address = address
        return None

    def validate_ssn(self,ssn):
        while len(self.ssn) != SSN_LEN:
            for char in self.ssn:
                if char.isdigit():
                    print(CORRECT_FORMAT) #Take out later
                    # Logic_Wrapper.register_crew(ssn)
                else:
                    print('This is not correct format.')
                    print('SSN has no digits')
                    self.ssn = input('Enter correct ssn: ') #sHOULD i put something else
            print('This is not correct format. SSN has 10 numbers')
            self.ssn = input('Enter correct ssn: ')

        def validate_name(self,name):
            # Name [just letters 3-30 - no numbers or symbol] -- maybe split functions for first and last name
            while not NAME_LEN_MINIMUM < self.name <= NAME_LEN_MAXIMUM:
                if not NAME_LEN_MINIMUM < self.name <= NAME_LEN_MAXIMUM:
                    print('This is incorrect input')
                    print('Input name lenght between 3 and 30 charachter')
                    self.name = input('Enter a name with correct lenght: ')
                else:
                    print(CORRECT_FORMAT)
                    first_name, last_name = name.strip().split()
                    Logic_Wrapper.register_crew(first_name, last_name)

        def validate_mobile_number(self, mobile):
            #Mobile number [just digits up to 15]
            while not MOBILE_LEN_MINIMUM >= len(self.mobile) >= MOLBILE_LEN_MAXIMUM :
                for char in self.mobile:
                    if char.isdigit():
                        print(CORRECT_FORMAT)
                        Logic_Wrapper.register_crew(mobile)
                    else:
                        print('This is not correct format.')
                        print('SSN has no digits')
                        self.mobile = input('Enter correct ssn: ') #sHOULD i put something else
                print('This is not valid format. SSN has 10 numbers')
                self.mobile = input('Enter correct ssn: ')


        def validate_address(self, address):
             # Address [just numbers and letters, dashes, spaces]
            string_punc = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
            while True:
                for char in self.addess: 
                    if char in string_punc:
                        print('This is not a valid address')
                        print('') 
                        self.address = input('Enter correct address: ')
                    else:
                        print(CORRECT_FORMAT)
                        Logic_Wrapper.register_crew(address)
                        break
        

        def validate_mobile_number(self, mobile):
            # Landline -- same as phone number probably
            while not MOBILE_LEN_MINIMUM >= len(self.mobile) >= MOLBILE_LEN_MAXIMUM :
                for char in self.mobile:
                    if char.isdigit():
                        print(CORRECT_FORMAT)
                        Logic_Wrapper.register_crew(mobile)
                    else:
                        print('This is not correct format.')
                        print('SSN has no digits')
                        self.mobile = input('Enter correct ssn: ') #sHOULD i put something else
                print('This is not valid format. Number should be between 7 and 15 numbers')
                self.mobile = input('Enter correct ssn: ')

        
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