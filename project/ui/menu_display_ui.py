import os
from model.voyage import Voyage
from datetime import datetime
from logic.logic_wrapper import Logic_Wrapper

QUIT_MENU = '[Q]UIT'
QUIT_MENU_BACK = '[M]ENU  [B]ACK  [Q]UIT'
QUIT_MESSAGE = "Quitting program"

UNDERSCORE = '_'
DASH = '-' * 68
HYPHEN = ':'
MULTIPLICATION_SIGN = '*'
NAN_AIR = 'NaN Air'
SPACE = ' '
PIPE = '|'
EQUAL_SIGN = '=' * 68


class Header_Footer_Display:
    def __init__(self):
        return None


    def display_main_header(self):
        print()
        print('\033[1;35;40m')
        print(' '*28,'||\    ||         ||\    ||')
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
        print('\033[1;37;40m')


    def display_main_footer_with_q_m_b(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{QUIT_MENU_BACK.center(67)}{HYPHEN:>2}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print('\033[1;37;40m')


    def display_lines_above_in_submenu(self):
        print(f'{HYPHEN:>15}{EQUAL_SIGN.center(67)}{HYPHEN}')
        print(f'{HYPHEN:>15}{HYPHEN:>69}')


    def display_lines_below_in_submenu(self):
        print(f'{HYPHEN:>15}{DASH.center(67)}{HYPHEN}')


class Menu_Display:
    def __init__(self):
        return None
    
    
    def display_main_menu(self):
        Header_Footer_Display.display_main_header(self)
        Header_Footer_Display.display_lines_above_in_submenu(self)
        sub_header = 'Main menu'
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer_Display.display_lines_below_in_submenu(self)

        menu_list = ['Crew members', 'Destination', 'Voyages', 'Aircraft']
        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer_Display.display_main_footer_with_q(self)


    def display_sub_menu(self, sub_header, menu_list):
        Header_Footer_Display.display_main_header(self)
        Header_Footer_Display.display_lines_above_in_submenu(self)
        print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
        Header_Footer_Display.display_lines_below_in_submenu(self)

        rest_of_lines = 10 - len(menu_list)

        for number , ele in enumerate(menu_list):
            print(f'{HYPHEN:>15}{(number+1):>10}   {ele:<55}{HYPHEN:>1}')
        for _ in range(rest_of_lines):
            print(f'{HYPHEN:>15}{HYPHEN:>69}')

        Header_Footer_Display.display_main_footer_with_q_m_b(self)


    def display_empty_list_menu(self, sub_header, menu_list, a_list):
            Header_Footer_Display.display_main_header(self)
            Header_Footer_Display.display_lines_above_in_submenu(self)
            print(f'{HYPHEN:>15}         {sub_header:<59}{HYPHEN:>1}')
            Header_Footer_Display.display_lines_below_in_submenu(self)

            rest_of_lines = 10 - len(menu_list)

            for number , (x, y) in enumerate(zip(menu_list, a_list)):
                print(f'{HYPHEN:>15}{(number+1):>10}   {(x + y):<55}{HYPHEN:>1}')
            for _ in range(rest_of_lines):
                print(f'{HYPHEN:>15}{HYPHEN:>69}')

            Header_Footer_Display.display_main_footer_with_q_m_b(self)


class Menu_Actions():
    def __init__(self):
        return None   

    def menu_input(self):
        '''Function that asks for menu number in the main menu UI.'''

        while True:
            Menu_Display.display_main_menu(self)
            command = input("Please enter menu number: ").lower()
            return command
        
    
    def clear_terminal():
        '''Function that clears the terminal screen.'''

        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
    
    
    def quit_program():
        '''Function that quits the program.'''

        command = input(f"Are you sure you want to quit? (Y/N) ")
        if command.lower() == "y":
            print(f"{QUIT_MESSAGE}")
            quit()
        else: 
            return None
