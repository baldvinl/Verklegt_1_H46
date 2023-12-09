from data.data_wrapper import Data_Wrapper
from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant


class Crew_Logic:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()

    def register_crew(self, crew):
        """Checks if crew object received is of the type 
        Pilot or not and forwards to data wrapper accordingly"""

        if isinstance(crew, Pilot):
            return self.data_wrapper.register_pilot(crew)
        else:
            return self.data_wrapper.register_flight_attendant(crew)

    def change_crew_info(self, ssn, changes):
        """ """
        crew_member = self.data_wrapper.get_crew_member(ssn)
        #for element in changes: [its a list of tuples]

        # go through list of changes and change attributes
        # check if pilot or not and return to data wrapper
        pass

    def display_all_crew(self):
        """Receives lists of pilots and flight attendants 
        from data wrapper, combines them and returns"""
        pilots_list = self.data_wrapper.display_pilots()
        flight_attendants_list = self.data_wrapper.display_flight_attendants()
        all_crew_list = pilots_list + flight_attendants_list
        return all_crew_list

    def get_crew_member(self, ssn):
        """Receives social security number of crew member and forwards to data wrapper"""
        return self.data_wrapper.get_crew_member(ssn)

    def availability_list(self, date, availability):
        """"""
        # specific day
        # get all voyages for that day from data [list of objects]
        # request pilots and flight attendants [list of objects]
        # [destination is in the voyage]
        # put all ssn from voyages into list [.captain, .pilot, .head_flight_attendant = attributes]
        # different for loop for working/ not working [working includes destinations]
        # for working tuple of [(employee, destination)] [check for destination in the for loops]
        # for loop employees and for ssn not in ssn list add employee to new list of non working [not working]
        pass
    
    def display_pilots(self):
        """Forwards request to data wrapper"""
        return self.data_wrapper.display_pilots()
    
    def display_flight_attendants(self):
        """Forwards requests to data wrapper"""
        return self.data_wrapper.display_flight_attendants()