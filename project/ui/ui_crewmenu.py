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

        print(f"1. Register Captain")
        print(f"2. Register First Officer")
        print(f"3. Register Head Flight Attendant.")
        print(f"4. Register Flight attendant.")   
        print(f"5. Crew records")
        print(f"6. Crew availability")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_crew(self, crew_type):
        '''Function that asks for input to register crew and returns crew information.'''

        current_menu = "Register crew"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)  

        if crew_type == "1":
            ssn = input("Enter SSN: ")
            name = input("Enter name: ")
            job_title = "Captain"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")
            type_rating = input("Enter type rating: ")

            new_crew_member = Pilot(ssn, name, job_title, address, email, mobile_no, phone_no, type_rating)
            return new_crew_member


        if crew_type == "2":
            ssn = input("Enter SSN: ")
            name = input("Enter name: ")
            job_title = "First Officer"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")
            type_rating = input("Enter type rating: ")

            new_crew_member = Pilot(ssn, name, job_title, address, email, mobile_no, phone_no, type_rating)
            return new_crew_member

        
        if crew_type == "3":    
            ssn = input("Enter SSN: ")
            name = input("Enter name: ")
            job_title = "Head Flight Attendant"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")

            new_crew_member = Flight_Attendant(ssn, name, job_title, address, email, mobile_no, phone_no)
            return new_crew_member

        if crew_type == "4":    
            ssn = input("Enter SSN: ")
            name = input("Enter name: ")
            job_title = "Flight Attendant"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")

            new_crew_member = Flight_Attendant(ssn, name, job_title, address, email, mobile_no, phone_no)
            return new_crew_member

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
                crew_entry = self.register_crew(command)
                print(crew_entry)
                wrapper = Logic_Wrapper
                wrapper.register_crew(wrapper, crew_entry)
                
            if command == '2':
                crew_entry = self.register_crew(command)
                wrapper = Logic_Wrapper
                wrapper.register_crew(wrapper, crew_entry)
                print(crew_entry)
            if command == '3':
                crew_entry = self.register_crew(command)
                wrapper = Logic_Wrapper
                wrapper.register_crew(wrapper, crew_entry)
                print(crew_entry)
            if command == '4':
                crew_entry = self.register_crew(command)
                wrapper = Logic_Wrapper
                wrapper.register_crew(wrapper, crew_entry)
                print(crew_entry)