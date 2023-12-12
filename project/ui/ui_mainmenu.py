import os
#from ui.ui_menu_display import Header_Footer
#from ui.ui_menu_display import Main_Menu

NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
QUIT_MESSAGE = "Quitting program"
current_menu = "Main menu"

class MainMenu_ui():
    def __init__(self):
        return None
    
    def main_menu(self):
        '''Function that displays the main menu UI.'''

        MainMenu_ui.clear_terminal()
        MainMenu_ui.main_header(current_menu)

        # Header_Footer.display_main_header(self)
        # Header_Footer.display_lines_below_in_submenu(self)
        # Main_Menu.display_main_menu_header(self)
        # Header_Footer.display_lines_below_in_submenu(self)
        # Main_Menu.display_main_menu(self)
        # Header_Footer.display_main_footer_with_q_m(self)
        

        print(f"1. Crew")
        print(f"2. Destinations")
        print(f"3. Voyages")
        print(f"4. Aircraft")
        print(f"5. Print options")
        
        print(f"{QUIT}")
    
    def input(self):
        '''Function that asks for menu number in the main menu UI.'''

        while True:
            self.main_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            return command
        
    def clear_terminal():
        '''Function that clears the terminal screen.'''

        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
    
    def main_header(current_menu):
        '''Reusable menu header for all menus.'''
        
        print(f"{NAME}")
        print(f"{TITLE}")
        print(f"{current_menu}")
    
    def quit_program():
        '''Function that quits the program.'''

        command = input(f"Are you sure you want to quit? (Y/N) ")
        if command.lower() == "y":
            print(f"{QUIT_MESSAGE}")
            quit()
        else: 
            return None
