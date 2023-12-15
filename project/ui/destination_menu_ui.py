from logic.logic_wrapper import Logic_Wrapper
from model.destination import Destination
from ui.menu_display_ui import *
from ui.print_lists_ui import List_Print_UI

ALLOWED_INPUT = ['m', 'q', 'b']


class DestinationMenu_ui():
    def __init__(self, data_connection: Logic_Wrapper, list_print: List_Print_UI):
        self.logic_wrapper = data_connection
        self.print_list = list_print
    
    def destination_display_menu(self):
        """Function that displays Destination Menu UI."""

        sub_header = 'Destination Menu'
        destination_menu_list = ['Register Destination', 'Display All Destinations', 'Edit Emergency Contact']

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, destination_menu_list)
    
    def get_destination_info_from_user(self):
        """Function that asks for inputs to register attributes for a destination and returns a destination object."""

        sub_header = 'Register Destination'

        command_list = ["Enter airport IATA: ", 
                        "Enter country: ", 
                        "Enter flight duration in hh:mm: ", 
                        "Enter distance in kilometers: ", 
                        "Enter emergency contact name: ", 
                        "Enter emergency contact phone number: "
                        ]
    
        menu_list = ['Airport IATA code:' , 'Country: ', 'Flight duration: ', 'Distance: ', 'Emergency name: ', 'Emergency number: ']

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
           
            answer = input('Press y if you want to save the destination: ')
            if answer == 'y':
                break
            
        new_destination = Destination()
        new_destination.attribute_implementation(input_list)

        return new_destination
    

    def display_all_destination_info(self):
        '''Function that displays the information about the destinations.'''

        Menu_Actions.clear_terminal()
        list_of_objects = self.logic_wrapper.get_all_destinations()
        self.print_list.display_destination_list(list_of_objects)
        
        command = input().lower()

        while command != ALLOWED_INPUT:
            continue 

    def change_emergency_contact_from_input(self):
        """Function that asks for ariport IATA and if they want to change either emergency 
        contact or number or both and returns a tuple"""

        question_ice_name = input("Would you like to change the emergency contact name? (press y for yes): ").lower()
        
        if question_ice_name == 'y':
            new_ice_name = input("Enter the new emergency contact name: ")
        else:
            new_ice_name = ''

        question_ice_number = input("Would you like to change the emergency contact number? (press y for yes): ").lower()

        if question_ice_number == 'y':
            new_ice_number = input("Enter the new emergency contact phone number: ")
        else:
            new_ice_number = ''

        return (new_ice_name, new_ice_number)


    def destination_input_display(self):
        '''Function that asks for input in destination menu.'''

        while True:
            self.destination_display_menu()
            command = input("Select menu option: ")

            if command == 'm':
                Menu_Actions.menu_input()

            elif command == "q":
                Menu_Actions.quit_program()

            elif command == "b":
                break
            
            elif command == '1':
                self.logic_wrapper.register_destination(self.get_destination_info_from_user())
                print("Destination has been registered!")
        
            elif command == '2':
                self.display_all_destination_info()

            elif command == '3':
                airport_iata = input("Enter the airport IATA code: ")
                emergency_contact_information = self.change_emergency_contact_from_input()
                self.logic_wrapper.change_emergency_contact_info(airport_iata, emergency_contact_information)
                print("Contact information has been updated!")