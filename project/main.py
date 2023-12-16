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
            crewmenu = CrewMenu_Ui(wrapper, listprint)
            crewmenu.crew_input_display()
            break
        elif command == '2':
            destinationmenu = DestinationMenu_ui(wrapper, listprint)
            destinationmenu.destination_input_display()
            break
        elif command == '3':
            voyagemenu = VoyageMenu_ui(wrapper, listprint)
            voyagemenu.voyage_input()
            break
        elif command == '4':
            aircraftmenu = AircraftMenu_ui(wrapper)
            aircraftmenu.aircraft_input()
            break
        elif command == '5':
            print("Print options")
            break
        elif command == "q":
            Menu_Actions.quit_program()
        elif command == "b":
            break
        