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
        command_list = ["Enter airport IATA: ", 
                        "Enter departure year from Iceland: ", 
                        "Enter departure month from Iceland: ", 
                        "Enter departure day from Iceland: ",  
                        "Enter departure year from destination: ", 
                        "Enter departure month from destination: ", 
                        "Enter departure day from destination: "
                        ]

        menu_list = ['Airport IATA Code: ', 'Departure year from Iceland: ', 'Departure month from Iceland: ', 'Departure day from Iceland: ', 'Departure year from destination: ', 'Departure month from destination: ', 'Departure day from destination: ']

        input_list = []

        while True:
            for i in range(0, 10):
                input_list.append('')

            for i in range(len(menu_list)):
                Menu_Actions.clear_terminal()
                Menu_Display.display_empty_list_menu(self, sub_header, menu_list, input_list)
                a = input(command_list[i])
                input_list[i] = a
                print()

            answer = input('Press y if you want to save the voyage: ')
            if answer == 'y':
                break

            
        departure_from_iceland = datetime(int(input_list[1]), int(input_list[2]), int(input_list[3]))
        departure_from_destination = datetime(int(input_list[4]), int(input_list[5]), int(input_list[6]))
        voyage_values = (input_list[0], departure_from_iceland, departure_from_destination)
        new_voyage = Voyage()
        new_voyage.attribute_implementation(voyage_values)
        
        return new_voyage

    def display_crew_allocation(self, date, working = bool):
        """Function that displays crew allocation for given date."""
        
        current_menu = f"Crew allocation on {date}"

        Menu_Actions.clear_terminal()

        crew_members_list = self.logic_wrapper.crew_status(date, working)

        self.print_list.display_flight_attendant_list(crew_members_list)
        
        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 

    def display_voyages_for_day(self, date):
        """Function that sends date to logic layer and prints all voyages on given date and if they are fully manned or not."""
        
        current_menu = f"Voyages on {date}"

        Menu_Actions.clear_terminal()

        voyage_list_for_day = self.logic_wrapper.get_voyages_for_period(date, 1)

        self.print_list.display_schedule_for_employees(voyage_list_for_day)

        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 
        
    def display_voyages_for_week(self, date):
        """Function that sends date to logic layer and prints all voyages a week from given date and if they are fully manned or not."""
        
        current_menu = f"Voyages in week after {date}"

        Menu_Actions.clear_terminal()

        voyage_list_for_week = self.logic_wrapper.get_voyages_for_period(date, 7)
        
        self.print_list.display_schedule_for_employees(voyage_list_for_week)

        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 

    def display_crew_availability(self):
        """Function that displays crew availability menu."""

        sub_header = "Display crew availability"

        menu_list = ['Working crew for given day',
                     'Not working crew for given day'
                    ]
        
        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)
    
        command = input("Enter menu number: ")

        if command == '1':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime(year, month, day, 0, 0, 0)           
            busy = True
            crew_status_list = self.logic_wrapper.crew_status(date, busy)
            self.print_list.display_schedule_for_all_crew(crew_status_list)
            command = input().lower()

            while command != ALLOWED_INPUT:
                continue 

        if command == '2':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime(year, month, day, 0, 0, 0)
            busy = False
            crew_status_list = self.logic_wrapper.crew_status(date, busy)
            self.print_list.display_schedule_for_all_crew(crew_status_list)
            command = input().lower()

            while command != ALLOWED_INPUT:
                continue    
    
    def add_crew_to_voyage(self):
        """get destination, departure date -> find voyage
        get crew free on departure date -> list
        """
        sub_header = 'Enter information for voyage you want to add crew to: '

        command_list = ["Enter destination airport: ", 
                        "Enter departure year from Iceland: ", 
                        "Enter departure month from Iceland: ", 
                        "Enter departure day from Iceland: "  
                        ]

        menu_list = ['Airport: ', 'Departure year from Iceland: ', 'Departure month from Iceland: ', 'Departure day from Iceland: ']

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
            
        departure_from_iceland = datetime(int(input_list[1]), int(input_list[2]), int(input_list[3]))
        crew_available = self.logic_wrapper.find_crew_for_voyage(departure_from_iceland)
        self.print_list.display_main_list(crew_available)


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
                voyage = self.register_voyage_from_input()
                self.logic_wrapper.register_voyage(voyage)

            elif command == '2':
                self.print_voyage_submenu()

            elif command == '3':
                self.add_crew_to_voyage()
            
            elif command == '4':
                self.display_crew_availability()