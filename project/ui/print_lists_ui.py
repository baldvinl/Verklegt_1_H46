from logic.logic_wrapper import Logic_Wrapper
from model.voyage import Voyage
from datetime import datetime

SSN = 'SSN'
NAME = 'Name'
JOB_TITLE = 'Job title'
ADDRESS = 'Address'
EMAIL = 'Email'
MOBILE = 'Mobile'
HOME_NR = 'Landline'
TYPE_RATING = 'License'
AIRPORT = 'Airport'
COUNTRY = 'Country'
FLIGHT_DURATION = 'Flight duration'
DISTANCE = 'Dinstance'
EMERGENCY_CONTACT_NAME = 'Emergency contact name'
EMERGENCY_CONTACT_NUMBER = 'Emergency number'

class List_Print_UI:
    def __init__(self,logic_connection: Logic_Wrapper):
        self.logic_wrapper = logic_connection

    def display_main_list(self, pilot_list):
        print()
        print('='*125)
        print(f'{SSN:<12}{NAME:<25}{ADDRESS:<15}{JOB_TITLE:<17}{EMAIL:<25}{MOBILE:<12}{HOME_NR:<12}{TYPE_RATING:<7}')
        print('-'*125)
        for pilot in pilot_list:
            print(f'{pilot.ssn:<12}{pilot.name:<25}{pilot.address:<15}{pilot.job_title:<17}{pilot.email:<25}{pilot.mobile_no:<12}{pilot.phone_no:<12}{pilot.type_rating:<7}')
        print('-'*125)


    def display_flight_attendant_list(self, flight_attendant_list):
        print()
        print('='*125, "\033[1m")
        print(f'{SSN:<12}{NAME:<25}{ADDRESS:<15}{JOB_TITLE:<17}{EMAIL:<25}{MOBILE:<12}{HOME_NR:<12}',"\033[0;0m")
        print('-'*125)
        for flight_attendant in flight_attendant_list:
            print(f'{flight_attendant.ssn:<12}{flight_attendant.name:<25}{flight_attendant.address:<15}{flight_attendant.job_title:<17}{flight_attendant.email:<25}{flight_attendant.mobile_no:<12}{flight_attendant.phone_no:<12}')
        print('-'*125)
    
    def display_one_crewmember_schedule(self, list_voyages):

        crew_member = self.logic_wrapper.get_crew_member(ssn)

        header = "Shift schedule for <name>, <SSN> within week <number>"
        subheader = "Destination"
        whitespace = " "

        country_list = []
        for voyage in list_voyages:
            work_date = datetime.strptime(voyage.time_depart_iceland["time_depart_iceland"], '%Y-%m-%d %H:%M')
            country_list.append((work_date, voyage.country))
        print()
        print(header)
        print("=" * 55)
        print(f"{whitespace:<10}{subheader:^45}")
        print("-" * 55)
        for (day, country) in country_list:
            print(f"{day:<10}{country:^45}")
        print("-" * 55)

    def display_destination_list(self, dest_list):
        print()
        print('='*100, "\033[1m")
        print(f'{AIRPORT:<9}{COUNTRY:<17}{FLIGHT_DURATION:^13}{DISTANCE:^15}{EMERGENCY_CONTACT_NAME:<25}{EMERGENCY_CONTACT_NUMBER:<12}',"\033[0;0m")
        print('-'*100)
        for destination in dest_list:
            print(f'{destination.airport:<9}{destination.country:<17}{destination.flight_duration:^13}{destination.distance:^15}{destination.ice_name:<25}{destination.ice_number:<12}')
        print('-'*100)
    
    def display_schedule_for_all_crew(self, a_list):
        print()
        print('='*120, "\033[1m")
        print(f'{SSN:<12}{NAME:<20}{ADDRESS:<15}{EMAIL:<22}{MOBILE:^12}{HOME_NR:^12}{JOB_TITLE:<16}{COUNTRY}',"\033[0;0m")
        print('-'*120)
        for crew_member in a_list:
            
            print(f'{crew_member.ssn:<12}{crew_member.name:<20}{crew_member.address:<15}{crew_member.email:<22}{crew_member.mobile:^12}{crew_member.phone_no:^12}{crew_member.job_title:<16}{crew_member.country} ')
        print('-'*120)

    



    
