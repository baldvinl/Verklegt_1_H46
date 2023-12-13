from datetime import date, timedelta
from data.data_wrapper import Data_Wrapper
from model.voyage import Voyage
from model.error_messages import ErrorMessages

class Voyage_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection

    def voyage_files_maintenance(self):
        """Forwards request to data wrapper"""
        return self.data_wrapper.move_voyages_done_to_file()

    def get_voyage(self, destination, departure) -> Voyage:
        """Requests voyage list, checks for a certain voyage with specific destination 
        and departure time from data wrapper, returns either voyage object or error code"""
        voyages = self.get_all_voyages()
        if voyages:
            for voyage in voyages:
                if voyage.destination == destination & voyage.time_depart_destination == departure:
                    return voyage
                else:
                    raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)
    
    def get_all_voyages(self) -> list:
        """Requests voyage list from data wrapper, checks if empty, if so returns error otherwise returns list"""
        voyage_list = self.data_wrapper.get_voyages_from_file()
        if voyage_list:
            return voyage_list
        else:
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)
    
    def register_voyage(self, new_voyage: Voyage):
        """Receives voyage object, checks if already in system, if so returns error code
        and if not forwards to data wrapper"""
        old_voyage = self.get_voyage(new_voyage.destination, new_voyage.time_depart_destination)
        if not old_voyage:
            return self.data_wrapper.register_voyage_to_file(new_voyage)
        else:
            raise ValueError(ErrorMessages.VOYAGE_ALREADY_IN_SYSTEM)

    def add_crew_to_voyage(self, crew_dict: dict, voyage: Voyage):
        """Receives crew dictionary separated by job titles, adds to voyage object receives and returns
        to data wrapper TODO need to update this to receive ("job title", ssn) and put ssns in the corresponding voyage attributes"""
        for job_title, crew_member in crew_dict.items():
            setattr(voyage, job_title, crew_member)
        return self.data_wrapper.register_updated_voyage_to_file(voyage)
    
    def add_aircraft_to_voyage(self, aircraft, destination, departure):
        """Gets voyage with certain destination & departure time, adds aircraft to it and returns to data wrapper"""
        voyage_to_add_aircraft = self.get_voyage(destination, departure)
        voyage_to_add_aircraft.aircraft = aircraft
        return self.data_wrapper.add_aircraft(aircraft)

    def get_voyage_status(self, destination, departure):
        """Receives destination and data and forwards to data wrapper TODO B requirement"""
        return self.data_wrapper.get_voyage_status(destination, departure)
    
    def check_date_past(self, date_input) -> bool:
        """checks if date given is in the past or not"""
        today = date.today()
        if today > date_input:
            return True
        else:
            return False

    def get_voyages_day(self, date_input):
        """Receives date, requests all voyages from data wrapper, if there is no voyages returns error
        if there is it returns voyages for that day in a list sorted #TODO MERGE THIS WITH BOTTOM"""
        all_voyages = self.get_all_voyages()
        if all_voyages:
            voyages_day = []
            for voyage in all_voyages:
                if voyage.departure_time == date_input:
                    voyages_day.append(voyage)
            sorted_voyages_day = sorted(voyages_day, key=lambda voyage: voyage.departure_time)
            return sorted_voyages_day
        else:
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)

    def get_voyages_week(self, date_input):
        """Receives date, requests all voyages from data wrapper, if there is no voyages returns error
        if there is it returns voyages for that week in a list sorted"""
        all_voyages = self.get_all_voyages()
        if all_voyages:
            voyages_week = []
            dates_week = []
            counter_date = date_input
            end_date = date_input + timedelta(days=6)
            while date_input <= end_date:
                dates_week.append(date_input)
                counter_date += 1
            for voyage in all_voyages:
                if voyage.departure_time in dates_week:
                    voyages_week.append(voyage)
            sorted_voyages_week = sorted(voyages_week, key=lambda voyage: (voyage.date, voyage.departure_time)) #not sure if this sorts properly
            return sorted_voyages_week
        else:
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)

    def get_voyage_schedule(self, ssn, first_day_of_week):
        """Receives ssn, and starting date of the week, checks them for the crew members ssn, and saves
        the one that have them listed. returns them in a list sorted. if there is no voyages it returns error code"""
        crew_members_voyages = []
        voyages_week = self.get_voyages_week(first_day_of_week)
        if voyages_week:
            job_title = ["captain", "pilot", "head flight attendant", "extra flight attendants"]
            for voyage in voyages_week:
                crew_in_voyage = []
                for job in job_title:
                    crew_in_voyage.append(getattr(voyage.job))
                if ssn in crew_in_voyage:
                    crew_members_voyages.append(voyage)
            crew_members_voyages_sorted = sorted(crew_members_voyages, key=lambda voyage:(voyage.date, voyage.departure_time))
            return crew_members_voyages_sorted
        else:
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)