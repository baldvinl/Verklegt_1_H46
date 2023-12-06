import os


NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"

class DestinationMenu_ui():
    def __init__(self):
        return None
    
    def destination_menu(self):
        '''Function that displays Destination Menu UI.'''

        current_menu = "Destination menu"

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

        print(f"1. Register a new destination")
        print(f"2. Destination info")
        print(f"3. Edit destination")

        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_destination(self):
        '''Function that asks for input to register destination and returns destination information.'''

        current_menu = "Register a new destination"

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

        country = input("Enter country: ")
        iata = input("Enter IATA code: ")
        duration = input("Enter flight duration in hh:mm: ")
        distance = input("Enter distance in kilometers: ")
        ice_name = input("Enter emergency contact name: ")
        ice_number = input("Enter emergency contact phone number: ")

        return country, iata, duration, distance, ice_name, ice_number

    def destination_info(self):
        '''Function that displays the information about a specific destination.'''
        
        current_menu = "Destination info"

        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

        iata = input("Enter IATA code: ")
        
        print(iata)

        pass


    def input(self):
        '''Function that asks for input in destination menu.'''

        while True:
            self.destination_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                return "q"
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                destination_entry = self.register_destination()
                print(destination_entry)
            if command == '2':
                self.destination_info()
            if command == '3':
                pass
                