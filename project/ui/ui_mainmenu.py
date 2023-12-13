import os
from ui.ui_menu_display import Display_Main_Menu

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
QUIT_MESSAGE = "Quitting program"
current_menu = "Main menu"

class MainMenu_ui():
    def __init__(self):
        return None
    
    def main_menu(self):
        '''Function that displays the main menu UI.'''

        MainMenu_ui.clear_terminal()
        Display_Main_Menu.display_main_menu(self)

    def input(self):
        '''Function that asks for menu number in the main menu UI.'''

        while True:
            self.main_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
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
