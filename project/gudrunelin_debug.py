from data.destination_data import Destination_Data
from data.crew_data import Crew_Data
from model.destination import Destination
from model.flight_attendant import Flight_Attendant
from model.pilot import Pilot

destination = Destination('LOL', 'Laughland', 'xx:xx', '909', 'changed', '55555')
data_class = Destination_Data()
iata = "KEF"

#reg_dest = data_class.register_destination_in_file(destination)
# get_dest = data_class.get_destination_from_file(iata)
#get_all_dest = data_class.get_destinations_from_file()
#print(destination.airport, destination.country, destination.flight_duration, destination.distance, destination.ice_name, destination.ice_number )
#reg_updated_des = data_class.register_updated_destination_to_file(destination)

#print(get_dest.airport, get_dest.country, get_dest.ice_name)

 #for elm in get_all_dest:
    #print(elm.airport, elm.country, elm.flight_duration, elm.distance, elm.ice_name, elm.ice_number)

pilot = Pilot('1122334455','John', 'Captain', 'CHANGED', 'John@captain.com', '6665555', '55874', 'FI-786')
flight_attendant = Flight_Attendant('9988776655', 'Rose', 'Head flight attendant', 'wateveralane 89', 'CHANGED', '6969691', '88464')
crew_class = Crew_Data()
ssn = '9988776655'

#reg_pilot = crew_class.register_pilot_to_file(pilot)
#reg_flight_at = crew_class.register_flight_attendant_to_file(flight_attendant)

# get_pilots = crew_class.get_pilots_from_file()
# get_flight_atts = crew_class.get_flight_attendants_from_file()

# for elm in get_pilots:
#     print(elm.ssn, elm.name, elm.type_rating, elm.phone_no)

# for elm in get_flight_atts:
#     print(elm.ssn, elm.address, elm.phone_no)

# get_crew_memb = crew_class.get_crew_member_from_file(ssn)

# print(get_crew_memb.name)
# pilot1 = Pilot('1122334455','John', 'Captain', 'UPDATED', 'John@captain.com', 'UPDATED', '55874', 'FI-786')
# flight_attendant1 = Flight_Attendant('9988776655', 'Rose', 'Head flight attendant', 'wateveralane 89', 'rose@titanic.com', 'UPDATED', '88464')
reg_upd_pilot = crew_class.register_updated_pilot_to_file(pilot)
reg_upd_flight_att = crew_class.register_updated_flight_attendant_to_file(flight_attendant)

