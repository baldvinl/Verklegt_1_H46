import os
from ui.ui_mainmenu import *

QUIT = "[Q]uit"


class CrewMenu_ui():
    def __init__(self):
        return None
    
    def crew_menu(self):
        '''Function that displays Crew Menu UI.'''

        current_menu = "Crew menu"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.menu_header(current_menu)

        print(f"1. Register crew")
        print(f"2. Crew records")
        print(f"3. Crew availability")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_crew(self):
        '''Function that asks for input to register crew and returns crew information.'''

        current_menu = "Register crew"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.menu_header(current_menu)        

        crew_name = input("Enter name: ")
        ssn = input("Enter SSN: ")
        address = input("Enter Address: ")
        mobile = input("Enter mobile phone number: ")
        home_phone = input("Enter home phone number: ")
        email = input("Enter e-mail: ")
        job_title = input("Enter job title: ")

        return crew_name, ssn, address, mobile, home_phone, email, job_title

    def input(self):
        '''Function that asks for input in crew menu.'''

        while True:
            self.crew_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                return "q"
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                crew_entry = self.register_crew()
                print(crew_entry)
            if command == '2':
                pass
            if command == '3':
                pass