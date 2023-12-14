from logic.logic_wrapper import Logic_Wrapper
from model.destination import Destination
from ui.menu_display_ui import *

ALLOWED_INPUT = ['m', 'q', 'b']


class DestinationMenu_ui():
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper
    
    def destination_display_menu(self):
        """Function that displays Destination Menu UI."""
        
        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self)
    
    def get_destination_info_from_user(self):
        """Function that asks for inputs to register attributes for a destination and returns a destination object."""

        command_list = ["Enter aiport iata : ", 
                        "Enter country: ", 
                        "Enter flight duration in hh:mm: ", 
                        "Enter distance in kilometers: ", 
                        "Enter emergency contact name: ", 
                        "Enter emergency contact phone number: "
                        ]
    
        menu_list = ['aiport iata : ', 'Country: ', 'Flight duration: ', 'Distance: ', 'Ice name: ', 'Ice number: ']

        input_list = []

        while True:
            for i in range(0, 10):
                input_list.append('')

            for i in range(len(menu_list)):
                Menu_Actions.clear_terminal()
                Menu_Display.display_empty_list_menu(self, menu_list, input_list)
                a = input(command_list[i])
                input_list[i] = a

            answer = input('Press y if you want to save the destination: ')
            if answer == 'y':
                break
            
        new_dest = Destination()
        new_dest.attribute_implementation(input_list)

        return new_dest
    

    def display_all_destination_info(self):
        '''Function that displays the information about the destinations.'''
        
        ##Kemur fall inn hér sem kallar á að prenta lista inn á viðmót með lista af objectum

        Menu_Actions.clear_terminal()        
        list_of_objects = self.logic_wrapper.get_all_destinations()
        
        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 

    def change_emergency_contact_from_input(self):
        """Function that asks for ariport IATA and if they want to change either emergency 
        contact or number or both and returns a tuple"""

        Menu_Actions.clear_terminal()

        question_ice_name = input("Would you like to change the emergency contact name (y/n): ").lower()
        question_ice_number = input("Would you like to change the emergency contact number (y/n): ").lower()

        if question_ice_name == 'y':
            new_ice_name = input("Enter the new emergency contact name: ")
        else:
            new_ice_name = ''

        if question_ice_number == 'n':
            new_ice_number = input("Enter the new emergency contact phone number: ")
        else:
            new_ice_number = ''

        return (new_ice_name, new_ice_number)


    def destination_input_display(self):
        '''Function that asks for input in destination menu.'''

        allowed_commands_input = ['m', 'q', 'b', '1', '2', '3']
        command_text = "Select menu option: "

        while command := (input(command_text)).lower() not in allowed_commands_input:
            self.destination_display_menu()

            if command == 'm':
                Menu_Display.display_main_menu()

            elif command == "q":
                Menu_Actions.quit_program()

            elif command == "b":
                break
            
            elif command == '1':
                self.logic_wrapper.register_destination(self.get_destination_info_from_user())
                break
          
            elif command == '2':
                self.display_all_destination_info()

            elif command == '3':
                airport_iata = input("Enter the airport IATA code: ")
                emergency_contact_information = self.change_emergency_contact_from_input()
                self.logic_wrapper.change_emergency_contact_info(airport_iata, emergency_contact_information)'
                