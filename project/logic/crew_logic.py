from data.data_wrapper import Data_Wrapper
from model.crew import Crew

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

    def display_working(self):
        return self.data_wrapper.display_working()