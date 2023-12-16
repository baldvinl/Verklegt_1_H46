from ui.menu_display_ui import *
from ui.destination_menu_ui import *
from ui.aircraft_menu_ui import *
from ui.crew_menu_ui import *
from ui.voyage_menu_ui import *
from ui.print_lists_ui import List_Display

wrapper = Logic_Wrapper()
listprint = List_Display(wrapper)

while True:
    command = Menu_Actions().menu_input()
    while True:
        if command == '1':
            crewmenu = CrewMenu_Ui(wrapper)
            command = crewmenu.crew_input_display()
            break
        if command == '2':
            destinationmenu = DestinationMenu_ui(wrapper, listprint)
            command = destinationmenu.destination_input_display()
            break
        if command == '3':
            voyagemenu = VoyageMenu_ui(wrapper, listprint)
            command = voyagemenu.voyage_input()
            break
        if command == '4':
            aircraftmenu = AircraftMenu_ui(wrapper)
            command = aircraftmenu.input()
            break
        if command == '5':
            print("Print options")
            break
        if command == "q":
            Menu_Actions.quit_program()
        if command == "b":
            break
        