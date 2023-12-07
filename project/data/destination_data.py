import csv
from model.destination import Destination


class Destination_Data:
    def __init__(self):
        self.file_name = "project/files/destinations.csv"

    def create_destination(self, destination):
        """Adds a new destination to the file"""
        
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["airport", "country", "flight_duration", "distance", "ice_name", "ice_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"airport": destination.airport, "country": destination.country, "flight_duration": destination.flight_duration, 
                             "distance": destination.distance, "ice_name": destination.ice_name, "ice_number": destination.ice_number})
            

    def display_destinations(self):
        """Returns a list of all destinations stored in the file"""

        dest_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dest_list.append(Destination(row["country"], row["airport"], row["flight_duration"], 
                                             row["distance"], row["ice_name"], row["ice_number"]))
        return dest_list
    

    def change_ice_name(self, iata, new_ice_name):
        """Changes the emergency contacts name"""

        with open(self.file_name, 'r+', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            rows = []
            for row in reader:
                if row["airport"] == iata:
                    row["ice_name"] = new_ice_name
                rows.append(row)

            csvfile.seek(0)
            fieldnames = ["airport", "country", "flight_duration", "distance", "ice_name", "ice_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            csvfile.truncate()


    def change_ice_number(self, iata, new_ice_number):
        """Changes the emergency contacts number"""
        
        with open(self.file_name, 'r+', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            rows = []
            for row in reader:
                if row["airport"] == iata:
                    row["ice_number"] = new_ice_number
                rows.append(row)

            csvfile.seek(0)
            fieldnames = ["airport", "country", "flight_duration", "distance", "ice_name", "ice_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            csvfile.truncate()
