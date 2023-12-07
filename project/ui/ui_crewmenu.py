import os
from ui.ui_mainmenu import *

from logic.logic_wrapper import Logic_Wrapper

from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant

QUIT = "[Q]uit"


class CrewMenu_ui():
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper
        self.crew = Crew
        self.pilot = Pilot
        self.flight_attendant = Flight_Attendant
        return None
    
    def crew_menu(self):
        '''Function that displays Crew Menu UI.'''

        current_menu = "Crew menu"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        print(f"1. Register crew")
        print(f"2. Crew records")
        print(f"3. Crew availability")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_crew(self):
        '''Function that asks for input to register crew and returns crew information.'''

        current_menu = "Register crew"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)  

        print(f"1. Register pilot")
        print(f"2. Register flight attendant.")   

        command = input("Please enter command: ")

        if command == "1":
            ssn = input("Enter SSN: ")
            crew_name = input("Enter name: ")
            captain = input("Captain? (Y/N) ")
            captain = captain.lower()
            if captain == "y":
                supervisor = True
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")
            type_rating = input("Enter type rating: ")

            return Pilot(ssn, crew_name, supervisor, address, area_code, email, mobile_no, phone_no, type_rating)

        if command == "2":
            ssn = input("Enter SSN: ")
            crew_name = input("Enter name: ")
            head = input("Head flight attendant? (Y/N) ")
            head = head.lower()
            if head == "y":
                supervisor = True
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")

            return Flight_Attendant(ssn, crew_name, supervisor, address, area_code, email, mobile_no, phone_no)

    def input(self):
        '''Function that asks for input in crew menu.'''

        while True:
            self.crew_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                MainMenu_ui.quit_program()
                pass
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                crew_entry = self.register_crew()
                wrapper = Logic_Wrapper
                wrapper.register_crew(crew_entry)
                print(crew_entry)
            if command == '2':
                pass
            if command == '3':
                pass