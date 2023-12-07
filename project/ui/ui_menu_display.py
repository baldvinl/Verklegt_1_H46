# -------GENERAL CONSTANTS AND SYMBOLS----------
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
TEN = '10'


UNDERSCORE = '_'
DASH = '-' * 68
HYPHEN = ':'
MULTIPLICATION_SIGN = '*'
NAN_AIR = 'NaN Air'
SPACE = ' '
PIPE = '|'
EQUAL_SIGN = '=' * 68

# -----MULTIPLE MENU OPTIONS-----
QUIT_MENU = '[M]ENU  [Q]UIT'
QUIT_MENU_BACK = '[M]ENU  [BACK]  [Q]UIT'

CREW_MEMBER_AVAILABILITY = 'Crew member availability'
CREW_MEMBER_LIST = 'List of crew'
PILOT_LIST = 'List of pilots'
FLIGHT_ATTENDANT_LIST = 'List of flight attendants'
AVAILABLE_CREW_GIVEN_DAY = 'Available crew for a given day'
DESTINATION_LIST = 'List of destinations'
DAY_SCHEDULE = 'Crew day schedule'
WEEK_SCHEDULE = 'Crew member week schedule'
AIRCRAFT_STATUS = 'Aircraft status'
PRINT_VOYAGES_ONE_DAY = 'Print voyages for 1 day'
PRINT_VOYAGES_ONE_WEEK = 'Print voyages for 1 week'

#------MAIN MENU CONSTANTS------------
MAIN_MENU = 'Main menu'
CREW = 'Crew'
DESTINATION = 'Destination'
VOYAGES = 'Voyages'
AIRCRAFT = 'Aircraft'
PRINT_OPTIONS = 'Print options'
PRUFA = 'Shift schedule for crew member within a specific week'

#------CREW_MEMBER MENU CONSTANTS---------
CREW_MEMBER_MENU = 'Crew'
REGISTER_CAPTAIN = 'Register captain'
REGISTER_PILOT = 'Register pilot'
REGISTER_HEAD_FLIGHT_ATTENDANT = 'Register head flight attendant'
REGISTER_FLIGHT_ATTENDANT = 'Register flight attendant'
CREW_MEMBER_RECORDS = 'Crew member records'

#-------DESTINATION MENU CONSTANTS----------
DESTINATION_MENU = 'Destinations'
REGISTER_DESTINATION = 'Register destination'
DESTINATION_INFO = 'Destination info'
EDIT_DESTINATION = 'Edit destination'

#------VOYAGE MENU CONTANTS-----------
VOYAGE_MENU = 'Voyages'
REGISTER_VOYAGE = 'Register voyage'
ADD_AIRCRAFT_VOYAGE = 'Add aircraft'
ADD_CREW_VOYAGE = 'Add crew'

# -----AIRCRAFT MENU CONSTANTS-----
AIRCRAFT_MENU = 'Aircrafts'
REGISTER_AIRCRAFT = 'Register aircraft'


#------COMMAND CONSTANTS-----------
COMMAND = 'Enter a menu number: '

class Inputs_Prompt:
    def __init__(self):
        return None
    def menu_number(self):
        print(f'{COMMAND:>35}')

class Header_Footer:
    def __init__(self):
        return None

    def get_main_header(self):
        print()
        print()
        print(' '*29,'||\    ||         ||\    ||')
        print(' '*29,'|| \   ||    ^    || \   ||      **' )
        print(' '*29,'||  \  ||  // \\\  ||  \  ||   ^  || ||__')
        print(' '*29,'||   \ || //___\\\ ||   \ ||  /_\ || ||')
        print(' '*29,'||    \||//     \\\||    \|| /   \|| ||')

    def get_main_footer_with_q_m(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{QUIT_MENU.center(67)}{HYPHEN:>2}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print()

    def get_main_footer_with_q_m_b(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{QUIT_MENU_BACK.center(67)}{HYPHEN:>2}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print()

class Main_Menu:
    def __init__(self):
        return None
    def get_main_menu(self):
        extra_lines = 7
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{MAIN_MENU:>18}{HYPHEN:>51}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{CREW:>11}{HYPHEN:>48}')
        print(f'{HYPHEN:>15}{TWO:>10}{DESTINATION:>13}{HYPHEN:>46}')
        print(f'{HYPHEN:>15}{THREE:>10}{VOYAGES:>9}{HYPHEN:>50}')
        print(f'{HYPHEN:>15}{FOUR:>10}{AIRCRAFT:>10}{HYPHEN:>49}')
        print(f'{HYPHEN:>15}{FIVE:>10}{PRINT_OPTIONS:>15}{HYPHEN:>44}')
        for _ in range(extra_lines):    
            print(f'{HYPHEN:>15}{HYPHEN:>69}')


class Crew_Member_Menu:
    def __init__(self):
        return None
    def get_crew_member_menu(self):
        extra_lines = 5
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{CREW_MEMBER_MENU:>13}{HYPHEN:>56}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{REGISTER_PILOT:>16}{HYPHEN:>43}')
        print(f'{HYPHEN:>15}{TWO:>10}{REGISTER_CAPTAIN:>18}{HYPHEN:>41}')
        print(f'{HYPHEN:>15}{THREE:>10}{REGISTER_HEAD_FLIGHT_ATTENDANT:>32}{HYPHEN:>27}')
        print(f'{HYPHEN:>15}{FOUR:>10}{REGISTER_FLIGHT_ATTENDANT:>27}{HYPHEN:>32}')
        print(f'{HYPHEN:>15}{FIVE:>10}{CREW_MEMBER_RECORDS:>21}{HYPHEN:>38}')
        print(f'{HYPHEN:>15}{SIX:>10}{CREW_MEMBER_AVAILABILITY:>26}{HYPHEN:>33}')
        print(f'{HYPHEN:>15}{SEVEN:>10}{CREW_MEMBER_LIST:>14}{HYPHEN:>45}')
        for _ in range(extra_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')
    
    def register_crew(self):
        pass
    def get_crew_record(self):
        pass
    def edit_crew_records(self):
        pass
    def check_crew_availability(self):
        print('Available crew for given day')
        # print('Shift schedule for crew on specific day')
        # print('Shift schedule for crew member within a specific week')
    def get_all_crew_list(self):
        print('All crew member list')
    def get_pilot_list(self):
        print('Pilot list')
    def get_flight_attentant_list(self):
        print('Flight attentant list')


class Destination_Menu:
    print('Register a new destination')
    # print('Destination info')
    # print('Edit destination')
    def register_new_destination(self):
        pass
    def destination_info(self):
        pass
    def edit_destination(self):
        pass

class Voyages_Menu:
    def register_new_voyage(self):
        print('Register a new voyage')
    def print_voyages(self):
        print('Print for 1 day')
        # print('Print for 1 week')
    # call a function crew avalability
    def add_aircraft(self):
        print('Add aircraft')
    def add_crew(self):
        print('Add crew')

class Aircraft_Menu:
    print('Register new aircraft')
    # print('Aircraft status')

class Print_Menu:
    print('Print crew member list')
    # print('Print pilot list')
    # print('Print flight attendant list')
    # print('Available crew for given day')
    # print('List of destinations')
    # print('Shift schedule for crew on specific day')
    # print('Shift schedule for crew member within a specific week')
    # print('Aircraft status')
    # print('Print voyages for 1 day')
    # print('Print voyages for 1 week')

    



