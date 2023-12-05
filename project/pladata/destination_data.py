import csv
from model.destination import Destination

class Destination_Data:
    def __init__(self):
        self.filename = "files/destinations.csv"

    def create_destination(self, destination):
        pass

    def display_destination(self):
        dest_list = []
        with open(self.filename, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                dest_list.append(Destination(line["country"], line["IATA"], line["flight_duration"], 
                                             line["distance"], line["ice_name"], line["ice_number"]))
        return dest_list
