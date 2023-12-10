import os
from ui.ui_mainmenu import *

from logic.logic_wrapper import Logic_Wrapper

from model.voyage import Voyage
from model.crew import Crew
from model.destination import Destination


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
        MainMenu_ui.main_header(current_menu)

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
        MainMenu_ui.main_header(current_menu)

        destination_iata = input("Enter destination IATA code: ")
        voyage_date = input("Enter voyage date: ")
        departure_time_from = input("Enter departure time from Iceland: ")
        departure_time_to = input(f"Enter departure time from {destination_iata}: ")
        
        return destination_iata, voyage_date, departure_time_from, departure_time_to

    def display_crew_availability():
        pass

    def display_available_crew(date):
        """Function that displays available crew for given date."""
        
        current_menu = f"Available crew on {date}"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        wrapper = Logic_Wrapper()
        available_crew = wrapper.availability_list(date)
        
        crew_info = Crew()

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone")
        for elem in available_crew:
            crew_info = elem
            print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()

        def display_crew_schedule_date(ssn, date):
        """Function that displays the schedule for a given crew number on date."""
        
        current_menu = f"Schedule for {ssn} on {date}"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        wrapper = Logic_Wrapper()
        schedule = wrapper.get_voyages_date(ssn, date) #need to confirm function call
        
        crew_info = Crew(schedule)

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone, Destination") 
        print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no, crew_info.destination end= " " "\n") # need to confirm how to get destination
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()

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
                wrapper = Logic_Wrapper()
                wrapper.register_voyage(voyage_entry)
                print(voyage_entry)
            if command == '2':
                pass
            if command == '3':
                pass