import os
import csv
from model.flight_attendant import Flight_Attendant
from model.pilot import Pilot

class Crew_Data:
    def __init__(self):
        self.file_pilots = "files/pilots.csv"
        self.file_flight_attendants = "files/flight_attendants.csv"
        self.file_out = "files/outfile.csv"


    def register_pilot_to_file(self, pilot):
        """Adds a new pilot to the file of pilots"""

        with open(self.file_pilots, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "ssn",
                "name",
                "job_title",
                "address",
                "email", 
                "mobile_no",
                "phone_no",
                "type_rating"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                "ssn": pilot.ssn, 
                "name": pilot.name, 
                "job_title": pilot.job_title, 
                "address": pilot.address, 
                "email": pilot.email, 
                "mobile_no": pilot.mobile_no, 
                "phone_no": pilot.phone_no, 
                "type_rating": pilot.type_rating}
            )

            csvfile.close()
    

    def register_flight_attendant_to_file(self, flight_attendant):
        """Adds a new flight attendant to the file of flight attendants"""

        with open(self.file_flight_attendants, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "ssn",
                "name",
                "job_title",
                "address",
                "email",
                "mobile_no",
                "phone_no",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                "ssn": flight_attendant.ssn, 
                "name": flight_attendant.name, 
                "job_title": flight_attendant.job_title, 
                "address": flight_attendant.address, 
                "email": flight_attendant.email, 
                "mobile_no": flight_attendant.mobile_no, 
                "phone_no": flight_attendant.phone_no
            })
            
            csvfile.close()
            

    def get_pilots_from_file(self):
        """Returns a list of all pilots stored in the file"""

        pilot_list = []
        with open(self.file_pilots, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pilot_list.append(Pilot(
                        row["ssn"], 
                        row["name"], 
                        row["job_title"], 
                        row["address"], 
                        row["email"], 
                        row["mobile_no"], 
                        row["phone_no"], 
                        row["type_rating"]
                ))
            
            csvfile.close()
        return pilot_list


    def get_flight_attendants_from_file(self):
        """Returns a list of all flight attendants stored in the file"""

        flight_attendants_list = []
        with open(self.file_flight_attendants, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_attendants_list.append(Flight_Attendant(
                        row["ssn"], 
                        row["name"], 
                        row["job_title"], 
                        row["address"], 
                        row["email"], 
                        row["mobile_no"], 
                        row["phone_no"]
                    ))
           
            csvfile.close()
        return flight_attendants_list
                    
                    
    def register_updated_pilot_to_file(self, pilot):
        """Adds all the pilots in new file and swaps out the old pilot for the new updated one"""

        fieldnames = [
            "ssn", 
            "name", 
            "job_title", 
            "address", 
            "email", 
            "mobile_no", 
            "phone_no", 
            "type_rating"
        ]

        with open(self.file_pilots, "r", newline="", encoding="utf-8") as infile, open(self.file_out, "w+", newline="", encoding="utf-8") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row["ssn"] == pilot.ssn:
                    row = {
                        "ssn": pilot.ssn, 
                        "name": pilot.name, 
                        "job_title": pilot.job_title, 
                        "address": pilot.address, 
                        "email": pilot.email, 
                        "mobile_no": pilot.mobile_no, 
                        "phone_no": pilot.phone_no,
                        "type_rating": pilot.type_rating
                    }
                writer.writerow(row)

            infile.close()
            outfile.close()

            file_temp = "files/file_temp.csv"
            os.rename(self.file_pilots, file_temp)
            os.rename(self.file_out, self.file_pilots)
            os.rename(file_temp, self.file_out)

    def register_updated_flight_attendant_to_file(self, flight_attendant):
        """Adds all the flight_attendants in new file and swaps out the old flight attendant for the new updated one"""
        
        fieldnames = [
            "ssn", 
            "name", 
            "job_title", 
            "address", 
            "email", 
            "mobile_no", 
            "phone_no"
        ]
        
        with open(self.file_flight_attendants, "r", newline="", encoding="utf-8") as infile, open(self.file_out, "w+", newline="", encoding="utf-8") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row["ssn"] == flight_attendant.ssn:
                    row = {
                        "ssn": flight_attendant.ssn, 
                        "name": flight_attendant.name, 
                        "job_title": flight_attendant.job_title, 
                        "address": flight_attendant.address, 
                        "email": flight_attendant.email, 
                        "mobile_no": flight_attendant.mobile_no, 
                        "phone_no": flight_attendant.phone_no,
                    }
                writer.writerow(row)
        
            infile.close()
            outfile.close()

            file_temp = "files/file_temp.csv"
            os.rename(self.file_flight_attendants, file_temp)
            os.rename(self.file_out, self.file_flight_attendants)
            os.rename(file_temp, self.file_out)

