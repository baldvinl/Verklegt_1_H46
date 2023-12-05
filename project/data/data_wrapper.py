from data.destination_data import Destination_Data

class Data_Wrapper:
    def __init__(self):
        self.destination_data = Destination_Data()
        
    def display_destinations(self):
        return self.destination_data.display_destinations()
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    def change_ice_name(self, aita, new_ice_name):
        return self.destination_data.change_ice_name(aita, new_ice_name)

    def change_ice_number(self, aita, new_ice_number):
        return self.destination_data.change_ice_name(aita, new_ice_number)
