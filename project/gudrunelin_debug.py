from data.destination_data import Destination_Data
from model.destination import Destination

temp = 'NEW NUMBER'
iata = 'IATA'
data_class = Destination_Data()
result = data_class.display_destination(iata)
for elem in result:
    print(elem.country, elem.airport, elem.ice_name, elem.ice_number)
