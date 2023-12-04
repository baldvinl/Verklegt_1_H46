
from UI.ui_mainmenu import MainMenu_ui
from UI.ui_crewmenu import CrewMenu_ui

mainmenu = MainMenu_ui()
command = mainmenu.input()
while True:
    if command == '1':
        crewmenu = CrewMenu_ui()
        crew_entry = crewmenu.register_crew()
        print(crew_entry)
        break
    if command == '2':
        print("Destinations")
        break
    if command == '3':
        print("Voyages")
        break
    if command == '4':
        print("Aircraft")
        break
    if command == '5':
        print("Print options")
        break
    if command == "q":
        break
        