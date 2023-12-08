import os
from project.ui.ui_mainmenu import MainMenu_ui

from project.logic.logic_wrapper import Logic_Wrapper

from project.model.crew import Crew
from project.model.pilot import Pilot
from project.model.flight_attendant import Flight_Attendant

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

        print(f"1. Register Captain")
        print(f"2. Register First Officer")
        print(f"3. Register Head Flight Attendant.")
        print(f"4. Register Flight attendant.")   

        command = input("Please enter command: ")

        if command == "1":
            ssn = input("Enter SSN: ")
            crew_name = input("Enter name: ")
            job_title = "Captain"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")
            type_rating = input("Enter type rating: ")

            return Pilot(ssn, crew_name, job_title, address, area_code, email, mobile_no, phone_no, type_rating)

        if command == "2":
            ssn = input("Enter SSN: ")
            crew_name = input("Enter name: ")
            job_title = "First Officer"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")
            type_rating = input("Enter type rating: ")

            return Pilot(ssn, crew_name, job_title, address, area_code, email, mobile_no, phone_no, type_rating)
        
        if command == "3":    
            ssn = input("Enter SSN: ")
            crew_name = input("Enter name: ")
            job_title = "Head Flight Attendant"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")

            return Flight_Attendant(ssn, crew_name, job_title, address, area_code, email, mobile_no, phone_no)

        if command == "4":    
            ssn = input("Enter SSN: ")
            crew_name = input("Enter name: ")
            job_title = "Flight Attendant"
            address = input("Enter address: ")
            area_code = input("Enter area code: ")
            email = input("Enter email: ")
            mobile_no = input("Enter mobile phone number: ")
            phone_no = input("Enter home phone number: ")

       return Flight_Attendant(ssn, crew_name, job_title, address, area_code, email, mobile_no, phone_no)


    def crew_information(self):
        '''Function that displays information on single crew member.'''

        current_menu = "Crew record"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        wrapper = Logic_Wrapper()
        info = wrapper.display_all_crew()

        loc_info = Crew()

        for elem in info:
            loc_info = elem
            print(f'SSN: {loc_info.ssn}')
            print(f'Name: {loc_info.name}')
            print(f'Job title: {loc_info.job_title}')
            print(f'Address: {loc_info.address}')
            print(f'Area code: {loc_info.area_code}')
            print(f'Email: {loc_info.email}')
            print(f'Mobile number: {loc_info.molbile_no}')
            print(f'Home phone:{loc_info.phone_no}')

            command = input('Please enter a command: ').lower()

            return command

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
                wrapper.register_crew(wrapper, crew_entry)
                print(crew_entry)
            if command == '2':
                pass
            if command == '3':
                pass