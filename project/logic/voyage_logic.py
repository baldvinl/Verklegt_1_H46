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

    def get_voyage(self, destination, departure) -> Voyage:
        """Requests voyage list, checks for a certain voyage with specific destination 
        and departure time from data wrapper, returns either voyage object or error code"""
        voyages = self.get_all_voyages()
        if voyages != ValidationLogic.NO_VOYAGES_FOUND:
            for voyage in voyages:
                if voyage.destination == destination & voyage.time_depart_destination == departure:
                    return voyage
                else:
                    return ValidationLogic.NO_VOYAGES_FOUND
    
    def get_all_voyages(self) -> list:
        """Requests voyage list from data wrapper, checks if empty, if so returns error otherwise returns list"""
        voyage_list = self.data_wrapper.get_voyages_from_file()
        if voyage_list:
            return voyage_list
        else:
            return ValidationLogic.NO_VOYAGES_FOUND
    
    def register_voyage(self, new_voyage: Voyage):
        """Receives voyage object, checks if already in system, if so returns error code
        and if not forwards to data wrapper"""
        voyage_check = self.get_voyage(new_voyage.destination, new_voyage.time_depart_destination)
        if voyage_check == ValidationLogic.NO_VOYAGES_FOUND:
            return self.data_wrapper.register_voyage_to_file(new_voyage)
        else:
            return ValidationLogic.ALREADY_IN_SYSTEM

    def find_crew_for_voyage(self, departure_time):
        """Receives date, requests crew not working on that date, returns dictionary with key: job title 
        and fills with all crew members separated by their job title, if there is no crew it returns
        error code"""
        busy = False
        job_title = ["captain", "pilot", "head flight attendant", "extra flight attendants"]
        crew_not_working = self.crew_logic.crew_status(departure_time, busy)
        if crew_not_working:
            crew_dict = dict.fromkeys(job_title, None)
            for member in crew_not_working:
                if member.job_title in crew_dict:
                    crew_dict[member.job_title].append(member)
            return crew_dict
        else: 
            return ValidationLogic.NO_CREW_FOUND

    def add_crew_to_voyage(self, crew_dict: dict, voyage: Voyage):
        """Receives crew dictionary separated by job titles, adds to voyage object receives and returns
        to data wrapper"""
        for job_title, crew_member in crew_dict.items():
            setattr(voyage, job_title, crew_member)
        return self.data_wrapper.register_updated_voyage_to_file(voyage)
    
    def add_aircraft_to_voyage(self, aircraft, destination, departure):
        """Gets voyage with certain destination & departure time, adds aircraft to it and returns to data wrapper"""
        voyage_to_add_aircraft = self.get_voyage(destination, departure)
        voyage_to_add_aircraft.aircraft = aircraft
        return self.data_wrapper.add_aircraft(aircraft)

    def get_voyage_status(self, destination, departure):
        """Receives destination and data and forwards to data wrapper TODO"""
        return self.data_wrapper.get_voyage_status(destination, departure)

    def get_voyages_day(self, date):
        """Receives date, requests all voyages from data wrapper, if there is no voyages returns error
        if there is it returns voyages for that day in a list sorted"""
        all_voyages = self.get_all_voyages()
        if all_voyages != ValidationLogic.NO_VOYAGES_FOUND:
            voyages_day = []
            for voyage in all_voyages:
                if voyage.date == date: # need to add date attribute to voyage model?
                    voyages_day.append(voyage)
            sorted_voyages_day = sorted(voyages_day, key=lambda voyage: voyage.departure_time)
            return sorted_voyages_day
        else:
            return ValidationLogic.NO_VOYAGES_FOUND

    def get_voyages_week(self, date):
        """Receives date, requests all voyages from data wrapper, if there is no voyages returns error
        if there is it returns voyages for that week in a list sorted"""
        all_voyages = self.get_all_voyages()
        if all_voyages:
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
        else:
            return ValidationLogic.NO_VOYAGES_FOUND

    def get_voyage_schedule(self, ssn, first_day):
        """Receives ssn, and starting date of the week, checks them for the crew members ssn, and saves
        the one that have them listed. returns them in a list sorted. if there is no voyages it returns error code"""
        crew_members_voyages = []
        voyages_week = self.get_voyages_week(first_day)
        if voyages_week != ValidationLogic.NO_VOYAGES_FOUND:
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
            return ValidationLogic.NO_VOYAGES_FOUND