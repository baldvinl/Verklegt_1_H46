import os

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
current_menu = "Main menu"

class MainMenu_ui():
    def __init__(self):
        return None
    
    def main_menu(self):
        '''Function that displays the main menu UI.'''

        MainMenu_ui.clear_terminal()
        MainMenu_ui.menu_header(current_menu)

        print(f"1. Crew")
        print(f"2. Destinations")
        print(f"3. Voyages")
        print(f"4. Aircraft")
        print(f"5. Print options")
        
        print(f"{QUIT}")
    
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
    
    def menu_header(current_menu):
        '''Reusable menu header for all menus.'''
        
        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")
    