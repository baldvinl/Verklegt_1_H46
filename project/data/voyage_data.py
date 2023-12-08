import csv
from model.voyage import Voyage

class Voyage_Data:
    def __init__(self):
        self.file_name = "files/voyage.csv"

    def create_voyage(self, voyage):
        """Adds a new voyage to the file"""

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["destination", "date", "time_depart_iceland", "time_depart_destination"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"destination": voyage.destination, "date": voyage.date, "time_depart_iceland": voyage.time_depart_iceland, 
                             "time_depart_destination": voyage.time_depart_destination})
            
    def register_crew_to_voyage(self, some_parameters):
        """Adds all crew members needed to a voyage"""


    def 

        
