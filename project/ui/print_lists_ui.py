from pprint import pprint
from logic.logic_wrapper import Logic_Wrapper
from model.pilot import Pilot

SSN = 'SSN'
NAME = 'Name'
JOB_TITLE = 'Job title'
ADDRESS = 'Address'
EMAIL = 'Email'
MOBILE = 'Mobile'
HOME_NR = 'Landline'
TYPE_RATING = 'License'

class List_Print_UI:
    def __init__(self,ssn, name, job_title, address, email, mobile, phone_no, type_rating, logic_connection: Logic_Wrapper):
        self.ssn = ssn
        self.name = name
        self.job_title = job_title
        self.address = address
        self.email = email
        self.molbile = mobile
        self.phone_no = phone_no
        self.type_rating = type_rating
        self.logic_wrapper = logic_connection

    def display_list(self, pilot_list):
        print()
        print('List of all pilots')
        print('='*125)
        print(f'{SSN:<12}{NAME:<25}{ADDRESS:<15}{JOB_TITLE:<17}{EMAIL:<25}{MOBILE:<12}{HOME_NR:<12}{TYPE_RATING:<7}')
        print('-'*125)
        for pilot in pilot_list:
            print(f'{pilot.ssn:<12}{pilot.name:<25}{pilot.address:<15}{pilot.job_title:<17}{pilot.email:<25}{pilot.mobile_no:<12}{pilot.phone_no:<12}{pilot.type_rating:<7}')
        print('-'*125)
        print()
        print()
        print()
        print()
        print()
            #     for number , ele in enumerate(menu_list):
            # print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
    
    