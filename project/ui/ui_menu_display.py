
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


#------COMMAND CONSTANTS-----------
COMMAND = 'Enter a menu number: '

class Inputs_Prompt:
    def __init__(self):
        return None
    def menu_number(self):
        print(f'{COMMAND:>35}')
        print()

class Header_Footer:
    def __init__(self):
        return None

    def display_main_header(self):
        print()
        print()
        print(' '*29,'||\    ||         ||\    ||')
        print(' '*29,'|| \   ||    ^    || \   ||      **' )
        print(' '*29,'||  \  ||  // \\\  ||  \  ||   ^  || ||__')
        print(' '*29,'||   \ || //___\\\ ||   \ ||  /_\ || ||')
        print(' '*29,'||    \||//     \\\||    \|| /   \|| ||')

    def display_main_footer_with_q_m(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{QUIT_MENU.center(67)}{HYPHEN:>2}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print()

    def display_main_footer_with_q_m_b(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{QUIT_MENU_BACK.center(67)}{HYPHEN:>2}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print()

    def lines_above_in_submenu(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')

    def display_lines_below_in_submenu(self):
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')

class Main_Menu:
    def __init__(self):
        return None
    
    def display_main_menu(self):
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Main menu'
        print(f'{HYPHEN:>15}{sub_header:>18}{HYPHEN:>51}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Employees', 'Destination', 'Voyages', 'Aircraft', 'Print options']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

class Employee_Menu:
    def __init__(self):
        return None
    
    def display_employees_menu(self):
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Employees'
        print(f'{HYPHEN:>15}{sub_header:>18}{HYPHEN:>51}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Register pilot', 'Register captain', 'Register flight attentant', 'Register head flight attentant', 'Employee record', 'Employee avaliability', 'List of employees']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

    def register_captain(self):
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register captain'
        print(f'{HYPHEN:>15}{sub_header:>25}{HYPHEN:>44}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: Yes', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ', 'Type rating: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

    def register_pilot(self):
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register pilot'
        print(f'{HYPHEN:>15}{sub_header:>25}{HYPHEN:>44}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: No', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ', 'Type rating: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

    def register_head_flight_attentant(self):
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register head flight_attentant'
        print(f'{HYPHEN:>15}{sub_header:>25}{HYPHEN:>44}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: Yes', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

    def register_flight_attentant(self):
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register flight_attentant'
        print(f'{HYPHEN:>15}{sub_header:>25}{HYPHEN:>44}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: No', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        
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

    



