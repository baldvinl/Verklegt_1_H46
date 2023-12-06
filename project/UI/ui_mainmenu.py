from tabulate import tabulate

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
current_menu = "Main menu"

class MainMenu_ui():
    def __init__(self):
        return None
    
    def main_menu(self):
        menu_options = [[1, "Crew"],
                  [2, "Destinations"],
                  [3, "Voyages"],
                  [4, "Aircraft"],
                  [5, "Print options"],]
        


        print(f"{NAME : ^60}")
        print(f"{TITLE : ^60}")
        print(f"{current_menu : ^60}")
        
        print(f"{QUIT : ^60}")
    
    def input(self):
        while True:
            self.main_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            return command