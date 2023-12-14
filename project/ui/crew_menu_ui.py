import os
from logic.logic_wrapper import Logic_Wrapper
from ui.menu_display_ui import *


QUIT = "[Q]uit"

class CrewMenu_ui():
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper
        self.pilot = Pilot
        self.flight_attendant = Flight_Attendant
        return None
    
    def crew_menu(self):
        '''Function that displays Crew Menu UI.'''

        current_menu = "Crew menu"

        MainMenu_ui.clear_terminal()
        Crew_Menu.display_employees_menu()

        print(f"1. Register Captain")
        print(f"2. Register First Officer")
        print(f"3. Register Head Flight Attendant.")
        print(f"4. Register Flight Attendant.")   
        print(f"5. Crew records")
        print(f"6. Crew availability")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_crew(self, crew_type):
        '''Function that asks for input to register crew and returns crew information.'''

        current_menu = "Register crew"

        MainMenu_ui.clear_terminal()
        # MainMenu_ui.main_header(current_menu)  

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
    
    def crew_records(self):
        """Function that displays the crew records menu and asks for input."""
        pass

    def display_pilots(self):
        """Function that displays all information about the pilots."""

        current_menu = "List of pilots"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        wrapper = Logic_Wrapper()
        info = wrapper.get_pilots() #need to confirm function call

        pilot_info = Pilot()

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone, Type rating")
        for elem in info:
            pilot_info = elem
            print(pilot_info.ssn, pilot_info.name, pilot_info.job_title, pilot_info.address, pilot_info.email, pilot_info.mobile_no, pilot_info.phone_no, pilot_info.type_rating, end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()

    def display_flight_attendants(self):
        """Function that displays all information about the flight attendants."""

        current_menu = "List of flight attendants"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        wrapper = Logic_Wrapper()
        info = wrapper.get_flight_attendants() #need to confirm function call

        fa_info = Flight_Attendant()

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone")
        for elem in info:
            fa_info = elem
            print(fa_info.ssn, fa_info.name, fa_info.job_title, fa_info.address, fa_info.email, fa_info.mobile_no, fa_info.phone_no, end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()

    def display_all_crew(self):
        """Function that displays all information about the crew."""

        current_menu = "List of crew members"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        wrapper = Logic_Wrapper()
        info = wrapper.get_all_crew() #need to confirm function call

        crew_info = Crew()

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone, Type rating") #how do we get the type rating for pilots?
        for elem in info:
            crew_info = elem
            print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no, crew_info.type_rating, end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()
    
    def display_crew_member(self, ssn):
        """Function that displays all information about a crew member."""

        current_menu = f"Information about crew member {ssn}"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        wrapper = Logic_Wrapper()
        info = wrapper.get_crew_member() #need to confirm function call

        crew_info = Crew(info)

        print(f"SSN, Name, Job title, Address, E-mail, Mobile, Phone, Type rating") #how do we get the type rating for pilots?
        print(crew_info.ssn, crew_info.name, crew_info.job_title, crew_info.address, crew_info.email, crew_info.mobile_no, crew_info.phone_no, crew_info.type_rating, end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()
    
    def change_crew_info(self):
        """Function that asks for crew SSN and updated information and returns."""
        
        current_menu = "Edit crew member information"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        new_crew_info = ()

        ssn = input("Enter the crew member's SSN: ")
        address = input("Enter address: ")
        area_code = input("Enter area code: ")
        email = input("Enter email: ")
        mobile_no = input("Enter mobile phone number: ")
        phone_no = input("Enter home phone number: ")

        new_crew_info = address, email, mobile_no, phone_no

        return ssn, new_crew_info


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
            if command == '5':
                pass
            if command == '6':
                pass
