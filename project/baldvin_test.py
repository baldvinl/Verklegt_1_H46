<<<<<<< HEAD

from ui.menu_display_ui import *

# from ui.crew_menu_ui import CrewMenu_ui
from ui.destination_menu_ui import DestinationMenu_ui
# from ui.aircraft_menu_ui import AircraftMenu_ui
# from ui.voyage_menu_ui import VoyageMenu_ui

QUIT_MESSAGE = "Quitting program"

run_program = True

while run_program:
    command = Menu_Actions().command_input()
=======
from ui.menu_display_ui import *
from ui.destination_menu_ui import *

run_program = True

while True:
    command = Menu_Actions().menu_input()
>>>>>>> gudrunelin
    while True:
        # if command == '1':
        #     crewmenu = CrewMenu_ui()
        #     command = crewmenu.input()
        #     break
        if command == '2':
<<<<<<< HEAD
            Menu_Actions.clear_terminal()
            command = DestinationMenu_ui().destination_display_menu()
=======
            destinationmenu = DestinationMenu_ui()
            command = destinationmenu.destination_input_display()
            break
        if command == '3':
            voyagemenu = VoyageMenu_ui()
            command = voyagemenu.input()
            break
        if command == '4':
            aircraftmenu = AircraftMenu_ui()
            command = aircraftmenu.input()
            break
        if command == '5':
            print("Print options")
            break
        if command == "q":
            Menu_Actions.quit_program()
        if command == "b":
>>>>>>> gudrunelin
            break
        # if command == '3':
        #     voyagemenu = VoyageMenu_ui()
        #     command = voyagemenu.input()
        #     break
        # if command == '4':
        #     aircraftmenu = AircraftMenu_ui()
        #     command = aircraftmenu.input()
        #     break
        # if command == '5':
        #     print("Print options")
        #     break
        # if command == "q":
        #     # MainMenu_ui.quit_program()
        # if command == "b":
        #     break
        