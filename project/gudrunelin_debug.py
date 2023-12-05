from data.destination_data import Destination_Data
from model.destination import Destination

temp = Destination()
data_class = Destination_Data()
data_class.create_destination(temp)
result = data_class.display_destinations()
for elem in result:
    print(elem.country, elem.airport, elem.distance)

