from data.destination_data import Destination_Data

data_class = Destination_Data()
result = data_class.display_destinations()
for elem in result:
    print(elem.country, elem.airport, elem.distance)