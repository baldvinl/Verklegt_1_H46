from data.crew_data import Crew_Data
from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant

class Crew_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_crew(self, crew):
        """Checks if crew object received is of the type 
        Pilot or not and forwards to data wrapper accordingly"""
        if isinstance(crew, Pilot):
            return self.data_wrapper.register_pilot(crew)
        else:
            return self.data_wrapper.register_flight_attendant(crew)

    def change_crew_info(self, crew):
        return self.data_wrapper.change_crew_info(crew)

    def display_all_crew(self):
        return self.data_wrapper.display_all_crew()

    def get_crew_info(self, ssn):
        return self.data_wrapper.get_crew_info(ssn)

    def display_not_working(self, date):
        return self.data_wrapper.display_not_working(date)

    def display_working(self, date):
        return self.data_wrapper.display_working(date)
    
    def display_pilots(self):
        return self.data_wrapper.display_pilots()
    
    def display_flight_attendants(self):
        return self.data_wrapper.display_flight_attendants()