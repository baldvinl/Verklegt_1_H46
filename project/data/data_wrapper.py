from data.destination_data import Destination_Data

class Data_Wrapper:
    def __init__(self):
        self.destination_data = Destination_Data()
        
    def display_destinations(self):
        return self.destination_data.display_destinations()
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
