import os
import csv
from datetime import datetime
from model.voyage import Voyage

class Voyage_Data:
    def __init__(self):
        self.file_voyages = "project/files/voyages.csv"
        self.file_out = "project/files/outfile.csv"
        self.file_voyages_done = "project/files/voyages_done.csv"


    def register_voyage_to_file(self, voyage):
        """Adds a new voyage to the file"""

        with open(self.file_voyages, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = [
                "destination",  
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
                "time_depart_iceland": voyage.time_depart_iceland, 
                "time_depart_destination": voyage.time_depart_destination,
                "captain": voyage.captain,
                "pilot": voyage.pilot,
                "head_flight_attendant": voyage.head_flight_attendant,
                "flight_attendant1": voyage.flight_attendant1,
                "flight_attendant2": voyage.flight_attendant2 
                })

            csvfile.close()
            
    
    def get_voyages_from_file(self):
        """Returns a list of all voyages stored in the file"""

        voyage_list = []
        with open(self.file_voyages, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voyage_list.append(Voyage(
                    row["destination"],
                    row["time_depart_iceland"], 
                    row["time_depart_destination"], 
                    row["captain"], 
                    row["pilot"], 
                    row["head_flight_attendant"], 
                    row["flight_attendant1"],
                    row["flight_attendant2"]
                    ))
            
            csvfile.close()
        return voyage_list
    

    def get_voyage_from_file(self, destination, departure):
        """Returns a class of a voyage with the corresponding destination and date"""

        with open(self.file_voyages, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date = datetime.strptime(row["time_depart_iceland"], '%Y-%m-%d %H:%M:%S')
                if row["destination"] == destination and date == departure:
                    return Voyage(
                        row["destination"], 
                        row["time_depart_iceland"], 
                        row["time_depart_destination"], 
                        row["captain"], 
                        row["pilot"], 
                        row["head_flight_attendant"],
                        row["flight_attendant1"],
                        row["flight_attendant2"]
                    )
            
            csvfile.close()
                
    
    def register_updated_voyage_to_file(self, voyage):
        """Adds all the voyages in new file and swaps out the old voyage for the new updated one"""

        fieldnames = [
            "destination",
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
                date = datetime.strptime(row["time_depart_iceland"], '%Y-%m-%d %H:%M:%S')

                if row['destination'] == voyage.destination and date == voyage.time_depart_iceland:
                    row = {
                        "destination": voyage.destination,
                        "time_depart_iceland": voyage.time_depart_iceland,
                        "time_depart_destination": voyage.time_depart_destination, 
                        "captain": voyage.captain, 
                        "pilot": voyage.pilot, 
                        "head_flight_attendant": voyage.head_flight_attendant,
                        "flight_attendant1": voyage.flight_attendant1,
                        "flight_attendant2": voyage.flight_attendant2
                    }
                writer.writerow(row)

            infile.close()
            outfile.close()

        file_temp = "project/files/file_temp.csv"
        os.rename(self.file_voyages, file_temp)
        os.rename(self.file_out, self.file_voyages)
        os.rename(file_temp, self.file_out)


    def move_voyages_done_to_file(self):
        """Moves all voyages that have already happend from the file voyages to the file voyages_done"""

        fieldnames = [
            "destination",
            "time_depart_iceland", 
            "time_depart_destination", 
            "captain", 
            "pilot", 
            "head_flight_attendant", 
            "flight_attendant1", 
            "flight_attendant2"
        ]

        with open(self.file_voyages, "r", newline="", encoding="utf-8") as infile, open(self.file_voyages_done, "a", newline="", encoding="utf-8") as outfile1, open(self.file_out, "w+", newline="", encoding="utf-8") as outfile2:
            reader = csv.DictReader(infile)
            writer1 = csv.DictWriter(outfile1, fieldnames=fieldnames)
            writer2 = csv.DictWriter(outfile2, fieldnames=fieldnames)

            writer2.writeheader()

            for row in reader:
                departure_iceland = datetime.strptime(row["time_depart_iceland"], '%Y-%m-%d %H:%M:%S')
                datetime_today = datetime.today()

                if departure_iceland < datetime_today:
                    writer1.writerow(row)

                else:
                    writer2.writerow(row)

            infile.close()
            outfile1.close()
            outfile2.close()

        file_temp = "project/files/file_temp.csv"
        os.rename(self.file_voyages, file_temp)
        os.rename(self.file_out, self.file_voyages)
        os.rename(file_temp, self.file_out)

        
