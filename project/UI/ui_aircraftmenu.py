
NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"


class AircraftMenu_ui():
    def __init__(self):
        return None
    
    def aircraft_menu(self):
        '''Function that displays Aircraft Menu UI.'''

        current_menu = "Aircraft menu"

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

        print(f"1. Register a new aircraft")
        print(f"2. Aircraft status")
        print(f"[M]enu  [B]ack  [Q]uit")
    
    def register_aircraft(self):
        '''Function that asks for input to register aircraft and returns aircraft information.'''

        current_menu = "Register a new aircraft"

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

        aircraft_name = input("Enter aircraft name: ")
        aircraft_type = input("Enter aircraft type: ")
        aircraft_manufacturer = input("Enter the aircraft manufacturer: ")
        seat_count = input("Enter the seat count: ")

        return aircraft_name, aircraft_type, aircraft_manufacturer, seat_count

    def aircraft_status(self):
        '''Function that displays the aircraft status.'''
        
        current_menu = "Aircraft status"

        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")

        date = input("Enter date: (YY-MM-DD) ")
        time = input("Enter time: (hh:mm) ")

        # Call function that returns list of aircraft and their status at the given date/time.

        pass

    def input(self):
        '''Function that asks for input in aircraft menu.'''

        while True:
            self.aircraft_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                return "q"
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                aircraft_entry = self.register_aircraft()
                print(aircraft_entry)
            if command == '2':
                pass
                