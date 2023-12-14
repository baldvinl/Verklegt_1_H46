
from ui.main_menu_ui import MainMenu_ui
from ui.crew_menu_ui import CrewMenu_ui
from ui.destination_menu_ui import DestinationMenu_ui
from ui.aircraft_menu_ui import AircraftMenu_ui
from ui.voyage_menu_ui import VoyageMenu_ui

QUIT_MESSAGE = "Quitting program"
    
run_program = True

while run_program:
    mainmenu = MainMenu_ui()
    command = mainmenu.input()
    while True:
        if command == '1':
            crewmenu = CrewMenu_ui()
            command = crewmenu.input()
            break
        if command == '2':
            destinationmenu = DestinationMenu_ui()
            command = destinationmenu.input()
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
            MainMenu_ui.quit_program()
        if command == "b":
            break
        