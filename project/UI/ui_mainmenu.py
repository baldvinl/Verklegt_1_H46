from tabulate import tabulate

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
current_menu = "Main menu"

class MainMenu_ui():
    def __init__(self):
        return None
    
    def main_menu(self):
        tabledata = [[1, "Crew"],
                  [2, "Destinations"],
                  [3, "Voyages"],
                  [4, "Aircraft"],
                  [5, "Print options"],]
        
        menu_table = tabulate(tabledata, tablefmt='simple_outline')

        print(f"{NAME : ^20}")
        print(f"{TITLE : ^20}")
        print(f"{current_menu : ^20}")
        print(menu_table)
        print(f"{QUIT : ^20}")
    
    def input(self):
        while True:
            self.main_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            return command