import os
from data.data_wrapper import Data_Wrapper
from ui.ui_mainmenu import *
from logic.logic_wrapper import *


#from data.destination_data import Destination_Data
from model.destination import Destination

QUIT = "[Q]uit"

class DestinationMenu_ui():
    def __init__(self):
        #self.data_wrapper = Data_Wrapper
        self.logic_wrapper = Logic_Wrapper
        return None
    
    def destination_menu(self):
        '''Function that displays Destination Menu UI.'''

        current_menu = "Destination menu"
        
        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        print(f"1. Register a new destination")
        print(f"2. Destination info")
        print(f"3. Edit destination")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_destination(self):
        '''Function that asks for input to register destination and returns destination information.'''

        current_menu = "Register a new destination"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        iata = input("Enter IATA code: ")
        country = input("Enter country: ")
        duration = input("Enter flight duration in hh:mm: ")
        distance = input("Enter distance in kilometers: ")
        ice_name = input("Enter emergency contact name: ")
        ice_number = input("Enter emergency contact phone number: ")
        
        new_dest = Destination(iata, country, duration, distance, ice_name, ice_number)

        return new_dest

    def destination_info(self):
        '''Function that displays the information about the destinations.'''
        
        current_menu = "Destination info"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        data_class = Logic_Wrapper()
        data = data_class.display_destinations()

        loc_info = Destination()

        print(f"IATA, Country, Distance, Flight duration, ICE Name, ICE Number")
        for elem in data:
            loc_info = elem
            print(loc_info.airport, loc_info.country, loc_info.distance, loc_info.flight_duration, loc_info.ice_name, loc_info.ice_number, end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter menu number: ")
        command = command.lower()

        return command


    def input(self):
        '''Function that asks for input in destination menu.'''

        while True:
            self.destination_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                MainMenu_ui.quit_program()
                pass
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                destination_entry = self.register_destination()
                data_class = Data_Wrapper()
                data_class.create_destination(destination_entry)
                print(destination_entry)
            if command == '2':
                self.destination_info()
                pass
            if command == '3':
                pass
                