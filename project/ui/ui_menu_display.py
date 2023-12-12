
QUIT_MENU = '[Q]UIT'
QUIT_MENU_BACK = '[M]ENU  [BACK]  [Q]UIT'

UNDERSCORE = '_'
DASH = '-' * 68
HYPHEN = ':'
MULTIPLICATION_SIGN = '*'
NAN_AIR = 'NaN Air'
SPACE = ' '
PIPE = '|'
EQUAL_SIGN = '=' * 68

class Header_Footer:
    def __init__(self):
        return None

    def display_main_header(self):
        print()
        print()
        print('\033[1;35;40m', ' '*27,'||\    ||         ||\    ||')
        print(' ' * 19,'_|_', ' ' * 4,'|| \   ||    ^    || \   ||      **',' ' * 9, '_|_')
        print(' ' * 16,'---(*)---',' ' * 1,'||  \  ||  // \\\  ||  \  ||   ^  || ||__',' ' * 1 , '---(*)---')
        print(' ' * 18,'\" \' \"',' ' * 3,'||   \ || //___\\\ ||   \ ||  /_\ || ||',' ' * 5 , '\" \' \"')
        print(' '*28,'||    \||//     \\\||    \|| /   \|| ||')

    def display_main_footer_with_q(self):
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
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Main menu'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Employees', 'Destination', 'Voyages', 'Aircraft', 'Print options']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q(self)

class Crew_Menu:
    def __init__(self):
        return None
    
    def display_crew_menu(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Crew'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Register captain', 'Register pilot', 'Register head flight attentant', 'Register flight attentant', 'Employee record', 'Employee avaliability', 'List of employees']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def register_captain(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register captain'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: Yes', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ', 'Type rating: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def register_pilot(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register pilot'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: No', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ', 'Type rating: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def register_head_flight_attentant(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register head flight attentant'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: Yes', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def register_flight_attentant(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register flight attentant'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Supervisor: No', 'Address: ', 'Area Code: ', 'Email: ', 'Mobile number: ', 'Phone number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def display_crew_records_menu(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Crew records'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['View crew member records', 'Edit crew member record', 'Print crew member list']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def view_crew_member_records(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'View crew member records'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def crew_member_records(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Crew member records'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Address: ', 'Area code: ', 'Email: ', 'Mobile number: ', 'Phone number: ', 'Job title: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def edit_crew_member_records_ssn(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Edit crew member records'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def edit_crew_member_records(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Edit crew member records'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['SSN: ', 'Name: ', 'Address: ', 'Area code: ', 'Email: ', 'Mobile number: ', 'Phone number: ', 'Job title: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)


    def check_employees_availability(self):
        pass
    def get_all_employees_list(self):
        pass
    def get_pilot_list(self):
        pass
    def get_flight_attentant_list(self):
        pass


class Destination_Menu:
    def __init__(self):
        return None
    
    def display_destination_menu(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Destination'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Register a new destination', 'Destination info', 'Edit destination']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def register_new_destination(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register destination'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Airport IATA code: ', 'Country: ', 'Flight duration: ', 'Distance: ', 'ICE name: ', 'ICE number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def destination_info(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Destination info'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['IATA code: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def destination_record(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Destination record'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['IATA code: ', 'Country: ', 'Flight duration: ', 'Distance: ', 'ICE name: ', 'ICE number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)      

    def edit_destination(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Edit destination'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['IATA code: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self) 

    def edit_destination_record(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Edit destination record'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['IATA code: ', 'Country: ', 'Flight duration: ', 'Distance: ', 'ICE name: ', 'ICE number: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self) 

class Voyages_Menu:
    def __init__(self):
        return None
    def display_voyage_menu(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Voyages'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Register voyage', 'Print voyage 1 day', 'Print voyages 1 week', 'Employee availability', 'Add aircraft', 'Add crew']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self) 

    def register_new_voyage(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register voyage'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Destination: ', 'Date: ', 'Time of departure from Iceland: ', 'Time of departure from destination: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self) 

    def print_voyages(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Print voyages'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Print for 1 day', 'Print for 1 week']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def add_aircraft(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Add aircraft to voyage'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Destination: ', 'Date: ', 'Time: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def add_crew(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Add crew to voyage'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Destination: ', 'Date: ', 'Time: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

class Aircraft_Menu:
    def __init__(self):
        return None
    
    def display_aircraft_menu(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Aircraft'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Register aircraft', 'Aircraft status']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def register_aircraft(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Register aircraft'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Name: ', 'Type: ', 'Manufacturer: ', 'Seat count: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)

    def aircraft_status(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Aircraft status'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Date: ', 'Time: ']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self)  

class Print_Menu:
    def __init__(self):
        return None
    
    def display_print_menu(self):
        Header_Footer.display_main_header(self)
        Header_Footer.lines_above_in_submenu(self)
        sub_header = 'Print menu'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer.display_lines_below_in_submenu(self)

        menu_list = ['Print crew list', 'Print pilot list', 'Print flight attendant list', 'Available crew for given day', 'List of destinations', 'Shift schedule for crew on specific day', 'Shift schedule for crew member within a specific week', 'Aircraft status', 'Print voyages for 1 day', 'Print voyages for 1 week']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer.display_main_footer_with_q_m_b(self) 


    



