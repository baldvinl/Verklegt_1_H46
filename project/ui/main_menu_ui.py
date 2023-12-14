import os
from ui.menu_display_ui import Main_Menu_Display

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
QUIT_MESSAGE = "Quitting program"
current_menu = "Main menu"

class MainMenu_ui():
    def __init__(self):
        return None
    
    def display_main_menu(self):
        '''Function that displays the main menu UI.'''

        MainMenu_ui.clear_terminal()
        Main_Menu_Display.display_main_menu(self)
    
    def input(self):
        '''Function that asks for menu number in the main menu UI.'''

        while True:
            self.display_main_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            return command
        
    def clear_terminal():
        '''Function that clears the terminal screen.'''

        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
    
    def main_header(current_menu):
        '''Reusable menu header for all menus.'''
        
        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")
    
    def quit_program():
        '''Function that quits the program.'''

        command = input(f"Are you sure you want to quit? (Y/N) ")
        if command.lower() == "y":
            print(f"{QUIT_MESSAGE}")
            quit()
        else: 
            return None
