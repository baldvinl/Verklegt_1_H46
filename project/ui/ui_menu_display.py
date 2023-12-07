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

QUIT_MENU = '[M]ENU  [Q]UIT'
QUIT_MENU_BACK = '[M]ENU  [BACK]  [Q]UIT'

EMPLOYEE_AVAILABILITY = 'Employee availability'
LIST_EMPLOYEE = 'List of employees'
PRINT_PILOT_LIST
PRINT_FLIGHT_ATTENDANT_LIST
AVAILABLE_EMPLOYEES_GIVEN_DAY
LIST_DESTINATION
AIRCRAFT_STATUS = 'Aircraft status'

UNDERSCORE = '_'
DASH = '-' * 68
HYPHEN = ':'
MULTIPLICATION_SIGN = '*'
NAN_AIR = 'NaN Air'
SPACE = ' '
PIPE = '|'
EQUAL_SIGN = '=' * 68

#------MAIN MENU CONSTANTS------------
MAIN_MENU = 'Main menu'
EMPLOYEES = 'Employees'
DESTINATION = 'Destination'
VOYAGES = 'Voyages'
AIRCRAFT = 'Aircraft'
PRINT_OPTIONS = 'Print options'
PRUFA = 'Shift schedule for employee within a specific week'

#------EMPLOYEE MENU CONSTANTS---------
EMPLOYEE_MENU = 'Employees'
REGISTER_PILOT = 'Register pilot'
REGISTER_FLIGHT_ATTENDANT = 'Register flight attendant'
EMPLOYEE_RECORDS = 'Employee records'

#-------DESTINATION MENU CONSTANTS----------
REGISTER_DESTINATION = 'Register destination'
DESTINATION_INFO = 'Destination info'
EDIT_DESTINATION = 'Edit destination'

#------VOYAGE MENU CONTANTS-----------
REGISTER_VOYAGE = 'Register voyage'
PRINT_VOYAGE = 'Print voyage'
ADD_AIRCRAFT_VOYAGE = 'Add aircraft'
ADD_CREW_VOYAGE = 'Add crew'

# -----AIRCRAFT MENU CONSTANTS-----
REGISTER_AIRCRAFT = 'Register aircraft'

# -----PRINT OPTIONS MENU CONSTANTS-----


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
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{MAIN_MENU:>18}{HYPHEN:>51}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{EMPLOYEES:>11}{HYPHEN:>48}')
        print(f'{HYPHEN:>15}{TWO:>10}{DESTINATION:>13}{HYPHEN:>46}')
        print(f'{HYPHEN:>15}{THREE:>10}{VOYAGES:>9}{HYPHEN:>50}')
        print(f'{HYPHEN:>15}{FOUR:>10}{AIRCRAFT:>10}{HYPHEN:>49}')
        print(f'{HYPHEN:>15}{FIVE:>10}{PRINT_OPTIONS:>15}{HYPHEN:>44}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')


class Employee_Menu:
    def __init__(self):
        return None
    print('1 Register employees')
    # print('2 Employee records (get employ record, edit record)')
    # print('3 Employee availability3')
    # print('Employee lists (three lists(all, pilots and flight attentant))')
    def register_employees(self):
        pass
    def get_employees_record(self):
        pass
    def edit_employees_records(self):
        pass
    def check_employees_availability(self):
        print('Available employees for given day')
        # print('Shift schedule for employees on specific day')
        # print('Shift schedule for employee within a specific week')
    def get_all_employees_list(self):
        print('All employee list')
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
    # call a function employees avalability
    def add_aircraft(self):
        print('Add aircraft')
    def add_crew(self):
        print('Add crew')

class Aircraft_Menu:
    print('Register new aircraft')
    # print('Aircraft status')

class Print_Menu:
    print('Print employee list')
    # print('Print pilot list')
    # print('Print flight attendant list')
    # print('Available employees for given day')
    # print('List of destinations')
    # print('Shift schedule for employees on specific day')
    # print('Shift schedule for employee within a specific week')
    # print('Aircraft status')
    # print('Print voyages for 1 day')
    # print('Print voyages for 1 week')

    



