
from UI.ui_mainmenu import MainMenu_ui
from UI.ui_crewmenu import CrewMenu_ui
from UI.ui_destinationmenu import DestinationMenu_ui
from UI.ui_aircraftmenu import AircraftMenu_ui
from UI.ui_voyagemenu import VoyageMenu_ui

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
            print(f"{QUIT_MESSAGE}")
            run_program = False
            break
        if command == "b":
            break
        