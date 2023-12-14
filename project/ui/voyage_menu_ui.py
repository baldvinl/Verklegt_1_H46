import os
from datetime import datetime

from ui.main_menu_ui import *
from ui.menu_display_ui import Voyages_Menu_Display

from logic.logic_wrapper import Logic_Wrapper

from model.voyage import Voyage
from model.crew import Crew
from model.destination import Destination


NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"


class VoyageMenu_ui():
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper
        self.crew = Crew
        self.voyage = Voyage
        self.destination = Destination
        return None
    
    def voyage_menu(self):
        '''Function that displays the Voyage Menu UI.'''


        MainMenu_ui.clear_terminal()
        Voyages_Menu_Display.display_voyage_menu(self)

    def register_voyage(self):
        '''Function that asks for input to register a new voyage and returns voyage information.'''

        current_menu = "Register a new voyage"

        MainMenu_ui.clear_terminal()
        # Voyages_Menu_Display.

        destination_iata = input("Enter destination IATA code: ")
        voyage_date = input("Enter voyage date: ")
        departure_time_from = input("Enter departure time from Iceland: ")
        departure_time_to = input(f"Enter departure time from {destination_iata}: ")

        new_voyage = Voyage(destination_iata, voyage_date, departure_time_from, departure_time_to)
        
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
                command = self.display_crew_availability()
    