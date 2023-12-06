import os
from ui.ui_mainmenu import *

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"


class VoyageMenu_ui():
    def __init__(self):
        return None
    
    def voyage_menu(self):
        '''Function that displays the Voyage Menu UI.'''

        current_menu = "Voyage menu"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.menu_header(current_menu)

        print(f"1. Register a new voyage")
        print(f"2. Print voyages")
        print(f"3. Crew availability")
        print(f"3. Add aircraft to voyage")
        print(f"3. Add crew to voyage")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_voyage(self):
        '''Function that asks for input to register a new voyage and returns voyage information.'''

        current_menu = "Register a new voyage"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.menu_header(current_menu)

        destination_iata = input("Enter destination IATA code: ")
        voyage_date = input("Enter voyage date: ")
        departure_time_from = input("Enter departure time from Iceland: ")
        departure_time_to = input(f"Enter departure time from {destination_iata}: ")
        
        return destination_iata, voyage_date, departure_time_from, departure_time_to

    def input(self):
        '''Function that asks for input in voyage menu.'''

        while True:
            self.voyage_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                MainMenu_ui.quit_program()
                pass
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                voyage_entry = self.register_voyage()
                print(voyage_entry)
            if command == '2':
                pass
            if command == '3':
                pass