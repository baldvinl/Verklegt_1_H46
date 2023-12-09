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
    def __init__(self):
        return None
    def get_destination_menu(self):
        extra_lines = 9
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{DESTINATION_MENU:>21}{HYPHEN:>48}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{REGISTER_DESTINATION:>22}{HYPHEN:>37}')
        print(f'{HYPHEN:>15}{TWO:>10}{DESTINATION_INFO:>18}{HYPHEN:>41}')
        print(f'{HYPHEN:>15}{THREE:>10}{EDIT_DESTINATION:>18}{HYPHEN:>41}')
        for _ in range(extra_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

    def register_new_destination(self):
        pass
    def destination_info(self):
        pass
    def edit_destination(self):
        pass

class Voyages_Menu:
    def __init__(self):
        return None
    def get_voyage_menu(self):
        extra_lines = 6
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{VOYAGE_MENU:>16}{HYPHEN:>53}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{REGISTER_VOYAGE:>17}{HYPHEN:>42}')
        print(f'{HYPHEN:>15}{TWO:>10}{PRINT_VOYAGES_ONE_DAY:>25}{HYPHEN:>34}')
        print(f'{HYPHEN:>15}{THREE:>10}{PRINT_VOYAGES_ONE_WEEK:>26}{HYPHEN:>33}')
        print(f'{HYPHEN:>15}{FOUR:>10}{CREW_MEMBER_AVAILABILITY:>26}{HYPHEN:>33}')
        print(f'{HYPHEN:>15}{FIVE:>10}{ADD_AIRCRAFT_VOYAGE:>14}{HYPHEN:>45}')
        print(f'{HYPHEN:>15}{SIX:>10}{ADD_CREW_VOYAGE:>10}{HYPHEN:>49}')
        for _ in range(extra_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')
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
    def __init__(self):
        return None
    def get_aircraft_menu(self):
        extra_lines = 10
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{AIRCRAFT_MENU:>18}{HYPHEN:>51}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{REGISTER_AIRCRAFT:>19}{HYPHEN:>40}')
        print(f'{HYPHEN:>15}{TWO:>10}{AIRCRAFT_STATUS:>17}{HYPHEN:>42}')
        for _ in range(extra_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

class Print_Menu:
<<<<<<< Updated upstream
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
=======
    def __init__(self):
        return None
    def get_print_menu(self):
        extra_lines = 2
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{PRINT_OPTIONS:>22}{HYPHEN:>47}')
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{ONE:>10}{CREW_MEMBER_LIST:>14}{HYPHEN:>45}')
        print(f'{HYPHEN:>15}{TWO:>10}{PILOT_LIST:>16}{HYPHEN:>43}')
        print(f'{HYPHEN:>15}{THREE:>10}{FLIGHT_ATTENDANT_LIST:>27}{HYPHEN:>32}')
        print(f'{HYPHEN:>15}{FOUR:>10}{AVAILABLE_CREW_GIVEN_DAY:>32}{HYPHEN:>27}')
        print(f'{HYPHEN:>15}{FIVE:>10}{DESTINATION_LIST:>22}{HYPHEN:>37}')
        print(f'{HYPHEN:>15}{SIX:>10}{DAY_SCHEDULE:>19}{HYPHEN:>40}')
        print(f'{HYPHEN:>15}{SEVEN:>10}{WEEK_SCHEDULE:>27}{HYPHEN:>32}')
        print(f'{HYPHEN:>15}{EIGHT:>10}{AIRCRAFT_STATUS:>17}{HYPHEN:>42}')
        print(f'{HYPHEN:>15}{NINE:>10}{PRINT_VOYAGES_ONE_DAY:>25}{HYPHEN:>34}')
        print(f'{HYPHEN:>15}{TEN:>10}{PRINT_VOYAGES_ONE_WEEK:>26}{HYPHEN:>33}')
        for _ in range(extra_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')
>>>>>>> Stashed changes

    



