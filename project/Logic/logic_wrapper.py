from data.data_wrapper import Data_Wrapper
from logic.aircraft_logic import Aircraft_Logic
from logic.crew_logic import Crew_Logic
from logic.destination_logic import Destination_Logic
from logic.voyage_logic import Voyage_Logic

class Logic_Wrapper:
    def __init__(self) -> None:
        self.data_wrapper = Data_Wrapper()
        self.aircraft_logic = Aircraft_Logic(self.data_wrapper)
        self.crew_logic = Crew_Logic(self.data_wrapper)
        self.destination_logic = Destination_Logic(self.data_wrapper)
        self.voyage_logic = Voyage_Logic(self.data_wrapper)

    def register_crew(self, crew):
        """Takes crew object and forwards to data layer"""
        pass

    def register_destination(self, destination):
        """Takes destination object and forwards to data layer"""
        pass

    def register_voyage(self, voyage):
        """Takes voyage objects and forwards to data layer"""
        pass

    def register_aircraft(self, aircraft):
        """Takes aircraft objects and forwards to data layer"""
        pass

    # What is a good way to make changes to crew info for example? Do we need one function for each field
    # How to we write function that receives information from input 