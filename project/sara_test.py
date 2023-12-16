from log

class Menu_Display_Lists:
    def __init__(self, logic_connection: Logic_Wrapper):
        self.logic_wrapper = logic_connection
    
    def display_one_crewmember_schedule(self, ssn, list_voyages):

        crew_member = self.logic_wrapper.get_crew_member(ssn)

        header = f"Shift schedule for: {crew_member.name}, SSN: {crew_member.ssn}"
        subheader = "Destination"
        whitespace = " "

        country_list = []
        for voyage in list_voyages:
            work_date = datetime.strptime(voyage.time_depart_iceland["time_depart_iceland"], '%Y-%m-%d %H:%M')
            country_list.append((work_date, voyage.country))
        print()
        print(header)
        print("=" * 55)
        print(f"{whitespace:<10}{subheader:^45}")
        print("-" * 55)
        for (day, country) in country_list:
            print(f"{day:<10}{country:^45}")
        print("-" * 55)