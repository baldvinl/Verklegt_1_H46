from data.destination_data import Destination_Data


iata = 'IATA'
data_class = Destination_Data()
result = data_class.display_destination(iata)
print(result.airport, result.country, result.ice_name, result.ice_number)
