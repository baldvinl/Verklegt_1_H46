import csv
from Model.destination import Destination

class Destination_Data:
    def __init__(self):
        self.filename = "Files/destinations.csv"

    def create_destination(self, destination):
        pass

    def display_destination(self):
        with open(self.filename, newline='', encoding="utf-8") as csvfile:
            pass
