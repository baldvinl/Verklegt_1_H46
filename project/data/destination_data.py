import os
import csv

from model.destination import Destination

class Destination_Data:
    def __init__(self):
        self.file_destinations = "files/destinations.csv"
        self.file_out = "files/outfile.csv"


    def register_destination_in_file(self, destination):
        """Adds a new destination to the file"""

        with open(self.file_destinations, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "airport",
                "country",
                "flight_duration",
                "distance",
                "ice_name",
                "ice_number",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                "airport": destination.airport, 
                "country": destination.country, 
                "flight_duration": destination.flight_duration, 
                "distance": destination.distance, 
                "ice_name": destination.ice_name, 
                "ice_number": destination.ice_number
            })

            csvfile.close()
            
    
    def get_destination_from_file(self, airport_iata):
        """Returns the destination with the reletive airport_iata"""

        with open(self.file_destinations, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["airport"] == airport_iata:
                    destination = Destination(
                        row["airport"], 
                        row["country"], 
                        row["flight_duration"], 
                        row["distance"], 
                        row["ice_name"], 
                        row["ice_number"]
                    )
        return destination


    def get_destinations_from_file(self):
        """Returns a list of all destinations stored in the file"""

        dest_list = []
        with open(self.file_destinations, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dest_list.append(Destination(
                    row["airport"], 
                    row["country"], 
                    row["flight_duration"], 
                    row["distance"], 
                    row["ice_name"], 
                    row["ice_number"]
                ))
                
            csvfile.close()
        return dest_list
    
    
    def register_updated_destination_to_file(self, destination):
        """Adds all the destinations in new file and swaps out the old destination for the new updated one"""

        fieldnames = [
            "airport", 
            "country", 
            "flight_duration", 
            "distance", 
            "ice_name", 
            "ice_number"
        ]

        with open(self.file_destinations, "r", newline="", encoding="utf-8") as infile, open(self.file_out, "w+", newline="", encoding="utf-8") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row["airport"] == destination.airport:
                    row = {
                        "airport": destination.airport,
                        "country": destination.country, 
                        "flight_duration": destination.flight_duration, 
                        "distance": destination.distance, 
                        "ice_name": destination.ice_name, 
                        "ice_number": destination.ice_number
                    }
                writer.writerow(row)
            
            infile.close()
            outfile.close()

        file_temp = "files/file_temp.csv"
        os.rename(self.file_destinations, file_temp)
        os.rename(self.file_out, self.file_destinations)
        os.rename(file_temp, self.file_out)

