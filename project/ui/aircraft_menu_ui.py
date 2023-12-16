from logic.logic_wrapper import Logic_Wrapper
from ui.menu_display_ui import *
from model.aircraft import *

class AircraftMenu_ui:
    def __init__(self, data_connection: Logic_Wrapper):
        self.logic_wrapper = data_connection
    
    def aircraft_menu(self):
        '''Function that displays Aircraft Menu UI.'''

        sub_header = "Aircraft menu"
        aircraft_menu_list = ['Register aircraft']

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, aircraft_menu_list)
    
    def register_aircraft_display(self):
        '''Function that asks for input to register aircraft and returns aircraft information.'''

        sub_header = 'Under Construction'

        menu_list = ['Will be Availble Soon', 'Upgrade on the Way!', QUIT_MENU]

        Menu_Actions.clear_terminal()
        Menu_Display.display_sub_menu(self, sub_header, menu_list)

        command = input()

        if command == "m":
            Menu_Actions.menu_input(self)

        elif command == "q":
            Menu_Actions.quit_program()


    #     sub_header = 'Register aircraft'
    #     command_list = ['Enter aircraft name: ', 'Enter aircraft type: ', 'Enter the aircraft manufacturer: ', 'Enter the seat count: ']

    #     menu_list = ['Name: ', 'Type: ', 'Manufacturer: ', 'Seat count: ']

    #     input_list = [] 

    #     while True:
    #         for i in range(0, 10):
    #             input_list.append('')

    #         for i in range(len(menu_list)):
    #             Menu_Actions.clear_terminal()
    #             Menu_Display.display_empty_list_menu(self, sub_header, menu_list, input_list)
    #             a = input(command_list[i])
    #             input_list[i] = a

    #         answer = input('Press y if you want to save the destination: ')
    #         if answer != 'y':
    #             break

    #     new_aircraft = Aircraft()
    #     new_aircraft.attribute_implementation(input_list)

    #     Menu_Actions.clear_terminal()
    #     Menu_Display.display_empty_list_menu(self, sub_header, menu_list, input_list)

    #     return new_aircraft

    def aircraft_input(self):
        '''Function that asks for input in aircraft menu.'''
        
        while True:
            self.aircraft_menu()
            command = input('Select menu option: ').lower()

            if command == 'm':
                Menu_Actions.menu_input(self)

            elif command == "q":
                Menu_Actions.quit_program()

            elif command == "b":
                break
            
            elif command == '1':
                self.logic_wrapper.register_aircraft(self.register_aircraft_display())
                break
