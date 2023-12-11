from data.data_wrapper import Data_Wrapper
from model.voyage import Voyage
from logic.validation_check import ValidationLogic
from datetime import date, timedelta

class Voyage_Logic:
    def __init__(self, data_connection: Data_Wrapper):
        self.data_wrapper = data_connection
        self.crew_logic = None
    
    def setCrew(self, x):
        self.crew_logic = x

    def get_voyage(self, destination, departure):
        """Requests voyage for a certain destination and date from data wrapper TODO"""
        voyages = self.get_all_voyages()
        for voyage in voyages:
            if voyage.destination == destination & voyage.time_depart_destination == departure:
                return voyage
    
    def get_all_voyages(self):
        """Receives and forwards request to data wrapper"""
        return self.data_wrapper.get_voyages_from_file()
    
    def register_voyage(self, new_voyage: Voyage):
        """Receives voyage object and forwards to data wrapper TODO"""
        voyage = self.get_voyage(new_voyage.destination, new_voyage.time_depart_destination)
        if not voyage:
            return self.data_wrapper.register_voyage(new_voyage)
        else:
            return ValidationLogic.ALREADY_IN_SYSTEM

    # def get_crew_info(self, destination, departure):
    #     """Receives destination and date and forwards to data wrapper"""
    #     return self.data_wrapper.get_information(destination, departure)

    def find_crew_for_voyage(self, departure_time):
        """Receives date, requests crew not working on that date and returns dictionary with key: job title and fills with all
        crew members separated by their job title"""
        # list of employees not working on this day - import from crew logic file and use the function there
        availability = False
        crew_not_working = self.crew_logic.availability_list(departure_time, availability)
        # make dict with key: job_title and fill with crew
        job_title = ["captain", "pilot", "head flight attendant", "extra flight attendants"]
        crew_dict = dict.fromkeys(job_title, None)
        for member in crew_not_working:
            if member.job_title in crew_dict:
                crew_dict[member.job_title].append(member)
        return crew_dict

    def add_crew_to_voyage(self, crew_dict: dict, voyage: Voyage):
        # receives crew to add
        # gets voyage from data
        for job_title, crew_member in crew_dict.items():
            setattr(voyage, job_title, crew_member)
        # returns new voyage object to data
        return voyage
    
    def add_aircraft_to_voyage(self, aircraft, destination, departure):
        """TODO"""
        # do we need to check if aircraft is already there and not allow them to replace it?
        voyage_to_add_aircraft = self.get_voyage( destination, departure)
        voyage_to_add_aircraft.aircraft = aircraft
        return voyage_to_add_aircraft

    def get_voyage_status(self, destination, departure):
        """Receives destination and data and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_status(destination, departure)

    def get_voyages_day(self, date):
        """Receive list from data wrapper, sorts by time and returns"""
        # sort by datetime
        # need to receive date only
        all_voyages = self.get_all_voyages()
        voyages_day = []
        for voyage in all_voyages:
            if voyage.date == date: # need to add date attribute to voyage model?
                voyages_day.append(voyage)
        sorted_voyages_day = sorted(voyages_day, key=lambda voyage: voyage.departure_time)
        return sorted_voyages_day

    def display_voyages_week(self, date):
        """"""
        # sort by datetime
        all_voyages = self.get_all_voyages()
        voyages_week = []
        dates_week = []
        counter_date = date
        end_date = date + timedelta(days=6)
        while date <= end_date:
            dates_week.append(date)
            counter_date += 1
        for voyage in all_voyages:
            if voyage.date in dates_week:
                voyages_week.append(voyage)
        sorted_voyages_week = sorted(voyages_week, key=lambda voyage: (voyage.date, voyage.departure_time)) #not sure if this sorts properly
        return sorted_voyages_week

    def get_voyage_schedule(self, ssn, departure):
        """Receives social security number and date and forwards to data wrapper"""
        return self.data_wrapper.get_voyage_schedule(ssn, departure)