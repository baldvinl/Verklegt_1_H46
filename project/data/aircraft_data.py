import csv
from model.aircraft import Aircraft

class Aircraft_Data:
    def __init__(self):
        self.file_name = "files/aircraft.csv"

    def create_aircraft(self, aircraft):
        """Adds a new aircraft to the file"""

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "type", "manufacturer", "seat_count"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"name": aircraft.name, "type": aircraft.type, "manufacturer": aircraft.manufacturer})

    

    