from data.crew_data import Crew_Data
from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant

class Crew_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_crew(self, crew):
        return self.data_wrapper.register_crew(crew)

    def change_crew_info(self, crew):
        return self.data_wrapper.change_crew_info(crew)

    def display_all_crew(self):
        return self.data_wrapper.display_all_crew()

    def get_crew_info(self, ssn):
        return self.data_wrapper.get_crew_info(ssn)

    def display_not_working(self, day):
        return self.data_wrapper.display_not_working(day)

    def display_working(self, day):
        return self.data_wrapper.display_working(day)
    
    def register_pilot(self, pilot):
        return self.data_wrapper.register_pilot(pilot)
    
    def display_pilots(self):
        return self.data_wrapper.display_pilots()
    
    def display_flight_attendants(self):
        return self.data_wrapper.display_flight_attendants
    
    def register_flight_attendant(self, flight_attendant):
        return self.data_wrapper.register_flight_attendant(flight_attendant)