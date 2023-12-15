from datetime import datetime
from logic.logic_wrapper import Logic_Wrapper
from ui.menu_display_ui import *
from model.voyage import *
from model.destination import *

class VoyageMenu_ui():
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper
    
    def voyage_menu(self):
        '''Function that displays the Voyage Menu UI.'''

        sub_header = 'Voyage Menu'
        voyage_menu_list = ['Register voyage', 'Print Voyages', 'Add Crew to Voyage']

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, voyage_menu_list)

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

        MainMenu_ui.clear_terminal()
        Voyages_Menu_Display.display_add_crew(self)

        wrapper = Logic_Wrapper()
        crew_availability = wrapper.availability_list(date, working)
        
        crew_info = Crew(), Destination()

        if working is True:
            print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone, Destination")
            for elem in crew_availability:
                crew_info = elem
                print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no, crew_info.airport, end= " " "\n")
            print(f"[M]enu  [B]ack  [Q]uit")
        else:
            print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone")
            for elem in crew_availability:
                crew_info = elem
                print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no, end= " " "\n")
            print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()
        
        return None

    def display_crew_schedule_date(self, ssn, date):
        """Function that displays the schedule for a given crew number for the week starting with date."""
        
        current_menu = f"Schedule for {ssn} on the week starting with {date}"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        wrapper = Logic_Wrapper()
        schedule = wrapper.get_voyages_date(ssn, date) #need to confirm function call
        
        crew_info = Crew(schedule)

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone, Destination") 
        print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no, crew_info.destination, end= " " "\n") # need to confirm how to get destination
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()

    def display_voyages_for_day(self, date):
        """Function that sends date to logic layer and prints all voyages on given date and if they are fully manned or not."""
        
        current_menu = f"Voyages on {date}"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        wrapper = Logic_Wrapper()
        voyages = wrapper.get_voyage_status(date)

        voyage_info = Voyage()
        
        for elem in voyages:
            voyage_info = elem
            print(voyage_info.destination, voyage_info.is_manned, end= " " "\n")

            return None
        
    def display_voyages_for_week(self, date):
        """Function that sends date to logic layer and prints all voyages a week from given date and if they are fully manned or not."""
        
        current_menu = f"Voyages in week after {date}"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        wrapper = Logic_Wrapper()
        voyages = wrapper.get_voyage_status(date)

        voyage_info = Voyage()
        
        for elem in voyages:
            voyage_info = elem
            print(voyage_info.destination, voyage_info.is_manned, end= " " "\n")

            return None

    def display_voyages(self):
        """Function that displays voyage menu"""

        current_menu = "Display voyages"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

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

        current_menu = "Display crew availability"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        print(f"1. Working crew for given day")
        print(f"2. Not working crew for given day")
        print(f"3. Print crew schedule for given week.")
    
        print(f"[M]enu  [B]ack  [Q]uit")

        command = input("Enter menu number: ")

        if command == '1':
            date = input("Enter date: ")
            working = True
            self.display_crew_allocation(date, working)
        if command == '2':
            date = input("Enter date: ")
            working = False
            self.display_crew_allocation(date, working)
        if command == '3':
            ssn = input("Enter SSN: ")
            date = input("Enter date: ")
            self.display_crew_schedule_date(ssn, date)
    
        return None    
    
    def input(self):
        '''Function that asks for input in voyage menu.'''

        while True:
            self.voyage_menu()
            command = input("Select menu option: ")
        
            if command == "m":
                Menu_Actions.menu_input()

            elif command == "q":
                Menu_Actions.quit_program()

            elif command == "b":
                break
            
            elif command == '1':
                self.logic_wrapper.register_voyage(self.register_voyage_from_input)

            elif command == '2':
                pass

            elif command == '3':
                pass
            
            elif command == "4":
                pass
    