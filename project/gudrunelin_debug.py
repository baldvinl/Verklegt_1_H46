from data.destination_data import Destination_Data
from model.destination import Destination

data_class = Destination_Data()
result = data_class.display_destinations()

for elm in result:
    print(elm.airport)
