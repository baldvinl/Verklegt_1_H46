import csv
from model.destination import Destination

class Destination_Data:
    def __init__(self):
        self.file_name = "files/destinations.csv"

    def create_destination(self, destination):
        """Adds a new destination to the file"""
        
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["country", "airport", "flight_duration", "distance", "ice_name", "ice_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"country": destination.country, "airport": destination.airport, "flight_duration": destination.flight_duration, 
                             "distance": destination.distance, "ice_name": destination.ice_name, "ice_number": destination.ice_number})


    def display_destinations(self):
        """Returns a list of all destinations stored in the file"""

        dest_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                dest_list.append(Destination(line["country"], line["airport"], line["flight_duration"], 
                                             line["distance"], line["ice_name"], line["ice_number"]))
        return dest_list
