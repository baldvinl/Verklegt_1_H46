import os
import csv
from model.voyage import Voyage

class Voyage_Data:
    def __init__(self):
        self.file_voyages = "project/files/voyage.csv"
        self.file_out = "project/files/outfile.csv"


    def register_voyage_to_file(self, voyage):
        """Adds a new voyage to the file"""

        with open(self.file_voyages, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = [
                "destination", 
                "date", 
                "time_depart_iceland", 
                "time_depart_destination", 
                "captain", 
                "pilot", 
                "head_flight_attendant", 
                "flight_attendant1", 
                "flight_attendant2"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                "destination": voyage.destination, 
                "date": voyage.date, 
                "time_depart_iceland": voyage.time_depart_iceland, 
                "time_depart_destination": voyage.time_depart_destination,
                "captain": voyage.captain,
                "pilot": voyage.pilot,
                "head_flight_attendant": voyage.head_flight_attendant,
                "flight_attendant1": voyage.flight_attendant1,
                "flight_attendant2": voyage.flight_attendant2 
                })
            
    
    def get_voyages_from_file(self):
        """Returns a list of all voyages stored in the file"""

        voyage_list = []
        with open(self.file_voyages, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voyage_list.append(Voyage(
                    row["destination"], 
                    row["date"], 
                    row["time_depart_iceland"], 
                    row["time_depart_destination"], 
                    row["captain"], 
                    row["pilot"], 
                    row["head_flight_attendant"], 
                    row["flight_attendant1"],
                    row["flight_attendant2"]
                    ))
        return voyage_list
    

    def get_voyage_from_file(self, destination, date):
        """Returns a class of a voyage with the corresponding destination and date"""

        with open(self.file_voyages, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["destination"] == destination and row["date"] == date:
                    return Voyage(
                        row["destination"], 
                        row["date"], 
                        row["time_depart_iceland"], 
                        row["time_depart_destination"], 
                        row["captain"], 
                        row["pilot"], 
                        row["head_flight_attendant"],
                        row["flight_attendant1"],
                        row["flight_attendant2"]
                    )
                
    
    def register_updated_voyage_to_file(self, voyage):
        """Adds all the voyages in new file and swaps out the old voyage for the new updated one"""

        fieldnames = [
            "destination",
            "date",
            "time_depart_iceland", 
            "time_depart_destination", 
            "captain", 
            "pilot", 
            "head_flight_attendant", 
            "flight_attendant1", 
            "flight_attendant2"
        ]

        with open(self.file_voyages, "r", newline="", encoding="utf-8") as infile, open(self.file_out, "w+", newline="", encoding="utf-8") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row["destination"] == voyage.destinastion and row["date"] == voyage.date:
                    row = {
                        "destination": voyage.destinastion,
                        "date": voyage.date,
                        "time_depart_iceland": voyage.time_depart_iceland,
                        "time_depart_destination": voyage.time_depart_destination, 
                        "captain": voyage.captain, 
                        "pilot": voyage.pilot, 
                        "head_flight_attendant": voyage.head_flight_attendant,
                        "flight_attendant1": voyage.flight_attendant1,
                        "flight_attendant2": voyage.flight_attendant2
                    }
                writer.writerow(row)

        file_temp = "project/files/file_temp.csv"
        os.rename(self.file_voyages, file_temp)
        os.rename(self.file_out, self.file_voyages)
        os.rename(file_temp, self.file_out)

        
