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

    def get_all_crew(self):
        """Receives lists of pilots and flight attendants 
        from data wrapper, combines them and returns"""
        pilots_list = self.data_wrapper.display_pilots()
        flight_attendants_list = self.data_wrapper.display_flight_attendants()
        all_crew_list = pilots_list + flight_attendants_list
        return all_crew_list
    
    def change_crew_info(self, ssn, changes):
        """Receives ssn, and changes list of tuples with format [(attribute_name, new_value)], requests crew member with ssn
        changes attributes with their new values and returns updated object to data wrapper"""
        crew_member = self.data_wrapper.get_crew_member(ssn)
        # for element in changes: [its a list of tuples]
        # go through and change attributes
        for attribute_name, new_value in changes:
            attribute_name_lower = attribute_name.lower()
            setattr(crew_member, attribute_name_lower, new_value)
        # check if pilot or not and return to data wrapper
        if isinstance(crew_member, Pilot):
            return self.data_wrapper.change_pilot_info(crew_member)
        else:
            return self.data_wrapper.change_flight_attendant_info(crew_member)

    def get_crew_member(self, ssn):
        """Receives social security number of crew member and forwards to data wrapper"""
        return self.data_wrapper.get_crew_member(ssn)

    def availability_list(self, date, availability):
        """"""
        # specific day
        # availability will be "working"/ "not working"
        # get all voyages for that day from data [list of objects]
        voyages_that_day = self.voyage_logic.get_voyages_day(date) # to be implemented in data - might need to change name
        # request pilots and flight attendants [list of objects]
        crew = self.get_all_crew()
        attributes_list = ["pilot", "captain", "head_flight_attendant", "extra_flight_attendants"]
        # [destination is in the voyage]
        # put all ssn from voyages into list [.captain, .pilot, .head_flight_attendant, .extra_flight_attendants = attributes]
        ssn_list = []
        for attribute in attributes_list:
            attribute_value = getattr(voyages_that_day, attribute)
            ssn_list.append(attribute_value)
        # different for loop for working/ not working [working should include destinations]
        # for working tuple of [(employee, destination)] [check for destination in the for loops]
        # for loop employees and for ssn not in ssn list add employee to new list of non working [not working]
        crew_not_working = []
        crew_working = []
        for crew_member in crew:
            if crew_member.ssn not in ssn_list:
                crew_not_working.append(crew_member)
            else:
                crew_working.append(crew_member, voyages_that_day.destination)
        if availability == "working":
            return crew_working
        else:
            return crew_not_working
    
    def display_pilots(self):
        """Forwards request to data wrapper"""
        return self.data_wrapper.display_pilots()
    
    def display_flight_attendants(self):
        """Forwards requests to data wrapper"""
        return self.data_wrapper.display_flight_attendants()