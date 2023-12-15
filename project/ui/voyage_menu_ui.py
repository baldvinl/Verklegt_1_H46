from datetime import datetime, date
from logic.logic_wrapper import Logic_Wrapper
from ui.menu_display_ui import *
from model.voyage import *
from model.destination import *
from ui.print_lists_ui import List_Print_UI

ALLOWED_INPUT = ['m', 'q', 'b']

class VoyageMenu_ui():
    def __init__(self, data_connection: Logic_Wrapper, display_connection: List_Print_UI):
        self.logic_wrapper = data_connection
        self.print_list = display_connection
    
    def voyage_menu(self):
        '''Function that displays the Voyage Menu UI.'''

        sub_header = 'Voyage Menu'
        voyage_menu_list = ['Register voyage', 'Print Voyages', 'Add Crew to Voyage', 'Display crew availability']

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, voyage_menu_list)

    def print_voyage_submenu(self):
        """Function that displays the print voyages sub menu and asks for input."""

        sub_header = 'Print Voyages'

        menu_list = ['Print voyages for one day',
                     'Print voyages for one week'
                    ]
        
        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)

        command = input("Enter menu number: ")

        if command == '1':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime(year, month, day, 0, 0, 0)
            self.display_voyages_for_day(date)
        if command == '2':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime(year, month, day, 0, 0, 0)
            self.display_voyages_for_week(date)

    def register_voyage_from_input(self):
        '''Function that asks for input to register a new voyage and returns voyage information.'''

        sub_header = 'Register voyage'
        command_list = ["Enter airport IATA: ", "Enter voyage date: ", "Enter departure time from Iceland: ", "Enter departure time from destination: "]

        menu_list = ['Airport IATA Code: ', 'Voyage Date: ', 'Departure time from Iceland: ', 'Enter departure time from destination: ']

        input_list = []

        while True:
            for i in range(0, 10):
                input_list.append('')

            for i in range(len(menu_list)):
                Menu_Actions.clear_terminal()
                Menu_Display.display_empty_list_menu(self, sub_header, menu_list, input_list)
                a = input(command_list[i])
                input_list[i] = a

            answer = input('Press y if you want to save the voyage: ')
            if answer == 'y':
                break

        new_voyage = Voyage()
        new_voyage.attribute_implementation(input_list)
        
        return new_voyage

    def display_crew_allocation(self, date, working = bool):
        """Function that displays crew allocation for given date."""
        
        current_menu = f"Crew allocation on {date}"

        Menu_Actions.clear_terminal()
        Menu_Display.display_main_menu(current_menu)

        crew_members_list = self.logic_wrapper.crew_status(date, working)

        self.print_list.display_flight_attendant_list(crew_members_list)
        
        command = input("Please enter command: ")
        command = command.lower()    

    def display_voyages_for_day(self, date):
        """Function that sends date to logic layer and prints all voyages on given date and if they are fully manned or not."""
        
        current_menu = f"Voyages on {date}"

        Menu_Actions.clear_terminal()
        Menu_Display.display_main_menu(current_menu)

        voyage_list_for_day = self.logic_wrapper.get_voyages_for_period(date, 1)

        self.print_list.display_destination_list(voyage_list_for_day)

        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 
        
    def display_voyages_for_week(self, date):
        """Function that sends date to logic layer and prints all voyages a week from given date and if they are fully manned or not."""
        
        current_menu = f"Voyages in week after {date}"

        Menu_Actions.clear_terminal()
        Menu_Display.display_main_menu(current_menu)

        voyage_list_for_week = self.logic_wrapper.get_voyages_for_period(date, 7)
        
        self.print_list.display_destination_list(voyage_list_for_week)

        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 

    def display_voyages(self):
        """Function that displays voyage menu"""

        current_menu = "Display voyages"

        Menu_Actions.clear_terminal()
        Menu_Display.display_main_menu(current_menu)

        print(f"1. Voyage fully manned for date")
        print(f"2. Voyage fully manned for week")
    
        print(f"[M]enu  [B]ack  [Q]uit")

        command = input("Enter menu number: ")

        if command == '1':
            date = input("Enter date: ")
            self.display_voyages_for_day(date)
        if command == '2':
            date = input("Enter date: ")
            self.display_voyages_for_week(date)
            
        return None
    
    def display_crew_availability(self):
        """Function that displays crew availability menu."""

        sub_header = "Display crew availability"

        # Menu_Actions.clear_terminal()
        # Menu_Display.display_main_menu(current_menu)

        menu_list = ['Working crew for given day',
                     'Not working crew for given day',
                     'Print crew schedule for given week'
                    ]
        
        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)

        # print(f"1. Working crew for given day")
        # print(f"2. Not working crew for given day")
        # print(f"3. Print crew schedule for given week.")
    
        command = input("Enter menu number: ")

        if command == '1':
            date = input("Enter date: ")
            working = True
            self.display_crew_allocation(date, working)
        if command == '2':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime(year, month, day, 0, 0, 0)
            working = False
            self.display_crew_allocation(date, working)
        if command == '3':
            ssn = input("Enter SSN: ")
            date = input("Enter date: ")
            self.display_crew_schedule_date(ssn, date)
    
    
    def voyage_input(self):
        '''Function that asks for input in voyage menu.'''

        while True:
            self.voyage_menu()
            command = input("Select menu option: ").lower()
        
            if command == "m":
                Menu_Actions.menu_input()

            elif command == "q":
                Menu_Actions.quit_program()

            elif command == "b":
                break
            
            elif command == '1':
                self.logic_wrapper.register_voyage(self.register_voyage_from_input) #TODO

            elif command == '2':
                self.print_voyage_submenu() #TODO

            elif command == '3':
                pass
            
            elif command == '4':
                self.display_crew_availability()