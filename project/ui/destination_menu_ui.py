import os
from ui.main_menu_ui import *
from ui.menu_display_ui import Destination_Menu_Display
from logic.logic_wrapper import Logic_Wrapper
from ui.menu_display_ui import Empty_Menu_Display

from model.destination import Destination

QUIT = "[Q]uit"

class DestinationMenu_ui():
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper
    
    def destination_menu(self):
        '''Function that displays Destination Menu UI.'''
        
        MainMenu_ui.clear_terminal()
        Destination_Menu_Display.display_destination_menu(self)
    
    def register_destination(self):
        '''Function that asks for input to register destination and returns destination information.'''

        # MainMenu_ui.clear_terminal()
        # MainMenu_ui.main_header(current_menu)
        # Destination_Menu_Display.display_register_destination(self)

        iata = "Enter IATA code: "
        country = "Enter country: "
        duration = "Enter flight duration in hh:mm: "
        distance = "Enter distance in kilometers: "
        ice_name = "Enter emergency contact name: "
        ice_number = "Enter emergency contact phone number: "

        a_list = []
        for i in range(0, 10):
            a_list.append('')

        command_list = [iata, country, duration, distance, ice_name, ice_number]
        menu_list = ['IATA code: ', 'Country: ', 'Flight duration: ', 'Distance: ', 'Ice name: ', 'Ice number: ']

        for i in range(len(menu_list)):
            MainMenu_ui.clear_terminal()
            Empty_Menu_Display.display_list_menu(self, menu_list, a_list)
<<<<<<< HEAD
            # print('\033[1;37;40m')
=======
>>>>>>> project
            a = input(command_list[i])
            a_list[i] = a
        


        # MainMenu_ui.clear_terminal()
        # Empty_Menu_Display.display_list_menu(self)
        
                # new_dest = Destination(a)

        # return new_dest

    def destination_info(self):
        '''Function that displays the information about the destinations.'''
        
        current_menu = "Destination info"

        MainMenu_ui.clear_terminal()
        # MainMenu_ui.main_header(current_menu)
        Destination_Menu_Display.display_destination_info(self)
        
        wrapper = Logic_Wrapper()
        info = wrapper.get_all_destinations()

        # loc_info = Destination()

        print(f"IATA, Country, Distance, Flight duration, ICE Name, ICE Number")
        for elem in info:
            loc_info = elem
            print(loc_info.airport, loc_info.country, loc_info.distance, loc_info.flight_duration, loc_info.ice_name, loc_info.ice_number, end= " " "\n")
        print(f"[M]enu  [B]ack  [Q]uit")
        
        command = input("Please enter command: ")
        command = command.lower()

        return command

    def change_ice_info(self):
        """Function that asks for location IATA and new ICE information and returns."""
        
        current_menu = "Edit destination ICE information"

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)
        
        new_ice_info = ()

        iata = input("Enter the location IATA code: ")
        new_ice_name = input("Enter the new emergency contact name: ")
        new_ice_number = input("Enter the new emergency contact phone number: ")
        new_ice_info = new_ice_name, new_ice_number


        return iata, new_ice_info



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
                wrapper = Logic_Wrapper()
                wrapper.register_destination(destination_entry)
                print(destination_entry)
            if command == '2':
                self.destination_info()
                pass
            if command == '3':
                new_ice_info = self.change_ice_info()
                wrapper = Logic_Wrapper()
                wrapper.change_ice_info(new_ice_info)
                pass
                