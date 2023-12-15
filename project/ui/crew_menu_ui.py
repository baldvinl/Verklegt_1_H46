import os
from logic.logic_wrapper import Logic_Wrapper
from ui.menu_display_ui import *
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant
from datetime import datetime

class CrewMenu_Ui():
    def __init__(self, logic_conneciton: Logic_Wrapper):
        self.logic_wrapper = logic_conneciton
    

    def display_crew_menu(self):
        '''Function that displays Crew Menu UI.'''

        sub_header = 'Crew Members'

        menu_list = ['Register Captain', 
                     'Register Pilot', 
                     'Register Head flight Attendant', 
                     'Register Flight Attendant', 
                     'Crew Member Information', 
                     'Crew Member Avaliability', 
                    ]

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)


    def register_crew_from_input(self, crew_type):
        '''Function that asks for input to register crew and returns crew information.'''

        sub_header = "Register crew"
        menu_list = ['Social Security Number ', 'Name', 'job_title', 'address', 'email', 'mobile_no', 'phone_no', 'type_rating']
        
        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)

        if crew_type == "1":

            while True:
                Menu_Actions.clear_terminal()
                Menu_Display.display_sub_menu(self, sub_header, menu_list)

                ssn = input("Enter SSN: ")
                name = input("Enter name: ")
                job_title = "Captain"
                address = input("Enter address: ")
                email = input("Enter email: ")
                mobile_no = input("Enter mobile phone number: ")
                phone_no = input("Enter home phone number: ")
                type_rating = input("Enter type rating: ")

                answer = input('Press y if you want to save the destination: ')
                if answer == 'y':
                    break

            return Pilot(ssn, name, job_title, address, email, mobile_no, phone_no, type_rating)


        elif crew_type == "2":
            while True:
                Menu_Actions.clear_terminal()
                Menu_Display.display_sub_menu(self, sub_header, menu_list)

                ssn = input("Enter SSN: ")
                name = input("Enter name: ")
                job_title = "Pilot"
                address = input("Enter address: ")
                email = input("Enter email: ")
                mobile_no = input("Enter mobile phone number: ")
                phone_no = input("Enter home phone number: ")
                type_rating = input("Enter type rating: ")

                answer = input('Press y if you want to save the destination: ')
                if answer == 'y':
                    break

            return Pilot(ssn, name, job_title, address, email, mobile_no, phone_no, type_rating)

        
        elif crew_type == "3":    
            while True:
                Menu_Actions.clear_terminal()
                Menu_Display.display_sub_menu(self, sub_header, menu_list)

                ssn = input("Enter SSN: ")
                name = input("Enter name: ")
                job_title = "Head flight attendant"
                address = input("Enter address: ")
                email = input("Enter email: ")
                mobile_no = input("Enter mobile phone number: ")
                phone_no = input("Enter home phone number: ")

                answer = input('Press y if you want to save the destination: ').lower()
                if answer == 'y':
                    break

            return Flight_Attendant(ssn, name, job_title, address, email, mobile_no, phone_no)

        elif crew_type == "4":

            while True:
                Menu_Actions.clear_terminal()
                Menu_Display.display_sub_menu(self, sub_header, menu_list)

                ssn = input("Enter SSN: ")
                name = input("Enter name: ")
                job_title = "Flight attendant"
                address = input("Enter address: ")
                email = input("Enter email: ")
                mobile_no = input("Enter mobile phone number: ")
                phone_no = input("Enter home phone number: ")

                answer = input('Press y if you want to save the destination: ')
                if answer == 'y':
                    break

            return Flight_Attendant(ssn, name, job_title, address, email, mobile_no, phone_no)
        else:
            Menu_Actions.menu_input()
            
    
    def crew_record_sub_menu(self):
        """Function that displays the crew records menu and asks for input."""

        sub_header = 'Crew Member Information'

        menu_list = ['View Crew Member Information', 
                     'Edit Crew Member Information', 
                     'List of All Crew Members'
                     'List of All Pilots',
                     'List of All Flight Attendants'
                    ]

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)

    
    def display_all_crew(self):
        """Function that displays all information about the crew."""

        current_menu = "List of crew members"

        Menu_Actions.clear_terminal()
        Menu_Display.m.main_header(current_menu)
        
        wrapper = Logic_Wrapper()
        info = wrapper.get_all_crew() #need to confirm function call

        crew_info = Crew()

    
    def display_pilots(self):
        """Function that displays all information about the pilots."""

        sub_header = "List of pilots"

        Menu_Actions.clear_terminal()
        Menu_Display.display_empty_list_menu(self, sub_header, )
        
        info = self.logic_wrapper.get_pilots() #need to confirm function call

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

        Menu_Actions.clear_terminal()
        Menu_Display.m
        
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

        Menu_Actions.clear_terminal()
        Menu_Display.m.main_header(current_menu)
        
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

        Menu_Actions.clear_terminal()
        Menu_Display.m.main_header(current_menu)
        
        new_crew_info = ()

        ssn = input("Enter the crew member's SSN: ")
        address = input("Enter address: ")
        area_code = input("Enter area code: ")
        email = input("Enter email: ")
        mobile_no = input("Enter mobile phone number: ")
        phone_no = input("Enter home phone number: ")

        new_crew_info = address, email, mobile_no, phone_no

        return ssn, new_crew_info
    
    def get_input_for_crew_schedule(self):
        """Function that displays the schedule for a given crew number for the week starting with date."""
        
        sub_header = "Crew Member: SSN and first day of the week"

        command_list = ["Enter the crew member's SSN: ", 
                        "Enter the year: ", 
                        "Enter the month: ", 
                        "Enter the day of the month: "
                        ]
        
        menu_list = ['Crew Members SSN: ', 'The Year: ', 'The Month: ', 'The Day of the Month: ']

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
        
            answer = input('Is The Information Correct (press y for yes): ')
            if answer == 'y':
                break

        ssn = input_list[0]
        year = input(input_list[1])
        month = input(input_list[2])
        day = input(input_list[3])

        start_date = datetime(year, month, day)

        list_voyages = self.logic_wrapper.get_weekly_voyage_schedule((ssn, start_date))
        Menu_Display_Lists.display_one_crewmember_schedule(ssn, list_voyages)


    def crew_input_display(self):
        '''Function that asks for input in crew menu.'''

        while True:
            self.display_crew_menu()
            command = input("Select menu option: ").lower()

            if command == "m":
                Menu_Actions.menu_input()

            elif command == "q":
                Menu_Actions.quit_program()

            elif command == "b":
                break

            elif command == '1' or command == '2' or command == '3' or command == '4':
                crew_entry = self.register_crew_from_input(command)
                self.logic_wrapper.register_crew(crew_entry)

            elif command == '5': #Crew Member record (sub menu)
                new_command = input("Select menu option: ").lower()
                if new_command == '1':
                    'View Crew Member Records'
                    pass

                elif new_command == '2':
                    'Edit Crew Member Records'
                    pass

                elif new_command == '3':
                    'List of All Crew Members'
                    pass

                elif new_command == '4':
                    'List of All Pilots'
                    pass

                elif new_command == '5':
                    'List of All Flight Attendants'
                    pass

            elif command == '6':
                self.get_input_for_crew_schedule()
