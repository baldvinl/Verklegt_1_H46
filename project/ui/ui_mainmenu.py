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

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

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