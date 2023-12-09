from data.destination_data import Destination_Data
from model.destination import Destination

destination = Destination()
data_class = Destination_Data()
iata = "KEF"

reg_dest = data_class.register_destination_in_file(destination)
get_dest = data_class.get_destination_from_file(iata)
get_all_dest = data_class.get_destinations_from_file()
reg_updated_des = data_class.register_updated_destination_to_file(destination)

print(get_dest.airport, get_dest.country, get_dest.ice_name)

# for elm in get_all_dest:
#     print(elm.airport, elm.country, elm.flight_duration, elm.distance, elm.ice_name, elm.ice_number)
