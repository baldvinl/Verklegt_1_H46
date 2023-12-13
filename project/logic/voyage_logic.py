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

    def get_voyage(self, destination, departure_time) -> Voyage:
        """Requests voyage list, checks for a certain voyage with specific destination 
        and departure time from data wrapper, returns either voyage object or error code"""
        if self.check_date_past(departure_time):
            voyages = self.get_past_voyages()
        else:
            voyages = self.get_future_voyages()
        if voyages:
            for voyage in voyages:
                if voyage.destination == destination & voyage.time_depart_destination == departure_time:
                    return voyage
                else:
                    raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)
    
    def get_all_voyages(self) -> list:
        """Requests past and future voyage lists from data wrapper, checks if empty, if so returns error otherwise returns list"""
        future_voyages = self.get_future_voyages()
        past_voyages = self.get_past_voyages()
        all_voyages = future_voyages + past_voyages
        if all_voyages:
            return all_voyages
        else:
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)
        
    def get_future_voyages(self) -> list:
        """Requests future voyage list from data wrapper, checks if empty, if so returns error otherwise returns list"""
        future_voyages = self.data_wrapper.get_future_voyages_from_file()
        if future_voyages:
            return future_voyages
        else:
            raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)

    def get_past_voyages(self) -> list:
        """Requests past voyage list from data wrapper, checks if empty, if so returns error otherwise returns list"""
        past_voyages = self.data_wrapper.get_past_voyages_from_file()
        if past_voyages:
            return past_voyages
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
        """Gets voyage with certain destination & departure time, adds aircraft to it and returns to data wrapper TODO B"""
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
        
    def get_voyages_for_period(self, starting_date, total_days):
        """Receives a starting date in datetime format, and total days of voyages to return. Requests all voyages from data wrapper
        makes a list of all the dates to be included in the final list. Goes through all voyages and keeps only the ones with the same dates.
        Sorts by departure time and returns list. If no voyages were initially received from data wrapper, it raises an error"""
        starting_date = starting_date.date
        all_voyages_list = self.get_all_voyages()
        if all_voyages_list:
            voyages_for_period = []
            dates_in_period = []
            end_date = starting_date + timedelta(days=total_days - 1)
            current_date = starting_date
            while current_date <= end_date:
                dates_in_period.append(current_date)
                current_date += timedelta(days=1)
            
            for voyage in all_voyages_list:
                if voyage.departure_time.date in dates_in_period:
                    voyages_for_period.append(voyage)
            
            sorted_voyages_for_period = sorted(voyages_for_period, key=lambda voyage: voyage.departure_time)
            return sorted_voyages_for_period
        raise ValueError(ErrorMessages.NO_VOYAGES_FOUND)

    def get_weekly_voyage_schedule(self, ssn, first_day_of_week):
        """Receives ssn, and starting date of the week, checks them for the crew members ssn, and saves
        the one that have them listed. returns them in a list sorted. if there is no voyages it returns error code"""
        crew_members_voyages = []
        voyages_week = self.get_voyages_for_period(first_day_of_week, 7)
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