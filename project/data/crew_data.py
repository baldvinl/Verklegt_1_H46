import csv
from model.flight_attendant import Flight_Attendant
from model.pilot import Pilot

class Crew_Data:
    def __init__(self):
        self.file_pilots = "files/pilots.csv"
        self.file_flight_attendants = "files/flight_attendants.csv"


    def register_pilot(self, pilot):
        """Adds a new pilot to the file of pilots"""

        with open(self.file_pilots, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["ssn", "name", "job_title", "area_code", "email", "mobile_no", "phone_no", "type_rating"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"ssn": pilot.ssn, "name": pilot.name, "job_title": pilot.job_title, "address": pilot.address, "area_code": pilot.area_code, 
                             "email": pilot.email, "mobile_no": pilot.mobile_no, "phone_no": pilot.phone_no, "type_rating": pilot.type_rating})
    

    def register_flight_attendant(self, flight_attendant):
        """Adds a new flight attendant to the file of flight attendants"""

        with open(self.file_flight_attendants, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["ssn", "name", "job_title", "area_code", "email", "mobile_no", "phone_no", "type_rating"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"ssn": flight_attendant.ssn, "name": flight_attendant.name, "job_title": flight_attendant.job_title, "address": flight_attendant.address, 
                             "area_code": flight_attendant.area_code, "email": flight_attendant.email, "mobile_no": flight_attendant.mobile_no, "phone_no": flight_attendant.phone_no})
            

    def display_pilots(self):
        """Returns a list of all pilots"""

        pilot_list = []
        with open(self.file_pilots, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pilot_list.append(Pilot(row["ssn"], row["name"], row["job_title"], 
                                             row["address"], row["area_code"], row["email"], row["mobile_no"], row["phone_no"], row["type_rating"]))
        return pilot_list


    def display_flight_attendants(self):
        """Returns a list of all flight_attendants"""

        flight_attendants_list = []
        with open(self.file_flight_attendants, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_attendants_list.append(Flight_Attendant(row["ssn"], row["name"], row["job_title"], 
                                             row["address"], row["area_code"], row["email"], row["mobile_no"], row["phone_no"]))
        return flight_attendants_list
    

    def display_crew_member_info(self, ssn):
        """Returns a class of crew member with the corresponding ssn"""

        with open(self.file_flight_attendants, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["ssn"] == ssn:
                    return Flight_Attendant(row["ssn"], row["name"], row["job_title"], row["address"], 
                                            row["area_code"], row["email"], row["mobile_no"], row["phone_no"])
                
        with open(self.file_pilots, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["ssn"] == ssn:
                    return Pilot(row["ssn"], row["name"], row["job_title"], row["address"], row["area_code"], 
                                 row["email"], row["mobile_no"], row["phone_no"], row["type_rating"])
                    
                    
    def change_pilot_info(self, ssn, changes): #changes is a list of tuples (header_name, changed_info)
        """Change attribute information for a pilot"""

        with open(self.file_pilots, 'r+', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            rows = []
            for row in reader:
                if row["ssn"] == ssn:
                    for elem in changes:
                        if row[elem[0]]:
                            row[elem[0]] = elem[1]
                rows.append(row)

            csvfile.seek(0)
            fieldnames = ["ssn", "name", "job_title", "address", "area_code", "email, mobile_no, phone_no, type_rating"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            csvfile.truncate()

    def change_flight_attendant_info(self, ssn, changes): #changes is a list of tuples (header_name, changed_info)
        """Change attribute information for a flight attendant"""

        with open(self.file_flight_attendants, 'r+', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            rows = []
            for row in reader:
                if row["ssn"] == ssn:
                    for elem in changes:
                        if row[elem[0]]:
                            row[elem[0]] = elem[1]
                rows.append(row)

            csvfile.seek(0)
            fieldnames = ["ssn", "name", "job_title", "address", "area_code", "email, mobile_no, phone_no"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            csvfile.truncate()