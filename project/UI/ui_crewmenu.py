
NAME = "NaN Air"
TITLE = "Crew planning software"
QUIT = "[Q]uit"
current_menu = "Crew menu"

class CrewMenu_ui():
    def __init__(self):
        return None
    
    def crew_menu(self):
        tabledata = [[1, "Register crew"],
                  [2, "Crew records"],
                  [3, "Crew availability"],]
        
        menu_table = tabulate(tabledata, tablefmt='simple_outline')

        print(f"{NAME : ^20}")
        print(f"{TITLE : ^20}")
        print(f"{current_menu : ^20}")
        print(menu_table)
        print(f"{QUIT : ^20}")
    
    def register_crew(self):
        print(f"{NAME : ^20}")
        print(f"{TITLE : ^20}")
        print(f"{current_menu : ^20}")
        name = input("Enter name: ")
        ssn = input("Enter SSN: ")
        address = input("Enter Address: ")
        mobile = input("Enter mobile phone number: ")
        home_phone = input("Enter home phone number: ")
        email = input("Enter e-mail: ")
        job_title = input("Enter job title: ")
        return name, ssn, address, mobile, home_phone, email, job_title

    def input(self):
        while True:
            self.crew_menu()
            command = input("Please enter menu number: ")
            command = command.lower()
            if command == "q":
                print("Quitting program")
                return "q"
            if command == "b":
                print("Going back to previous menu.")
                return "b"
            if command == '1':
                crew_entry = self.register_crew()
                