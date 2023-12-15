from ui.menu_display_ui import *
from ui.destination_menu_ui import *

run_program = True

while True:
    command = Menu_Actions().menu_input()
    while True:
        # if command == '1':
        #     crewmenu = CrewMenu_ui()
        #     command = crewmenu.input()
        #     break
        if command == '2':
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
        