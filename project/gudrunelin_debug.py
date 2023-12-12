from datetime import datetime
from data.destination_data import Destination_Data
from data.crew_data import Crew_Data
from model.destination import Destination
from model.flight_attendant import Flight_Attendant
from model.pilot import Pilot
from data.voyage_data import Voyage_Data
from model.voyage import Voyage

# destination = Destination('LOL', 'PAAAAAAA', 'xx:xx', '909', 'changed', '55555')
# data_class = Destination_Data()
# iata = "KEF"

#reg_dest = data_class.register_destination_in_file(destination)
# get_dest = data_class.get_destination_from_file(iata)
#get_all_dest = data_class.get_destinations_from_file()
#print(destination.airport, destination.country, destination.flight_duration, destination.distance, destination.ice_name, destination.ice_number )
#reg_updated_des = data_class.register_updated_destination_to_file(destination)

#print(get_dest.airport, get_dest.country, get_dest.ice_name)

 #for elm in get_all_dest:
    #print(elm.airport, elm.country, elm.flight_duration, elm.distance, elm.ice_name, elm.ice_number)

# pilot = Pilot('1122334455','John', 'Captain', 'CHANGED', 'John@captain.com', '6665555', '55874', 'FI-786')
# flight_attendant = Flight_Attendant('9988776655', 'Rose', 'Head flight attendant', 'wateveralane 89', 'CHANGED', '6969691', '88464')
# crew_class = Crew_Data()
# ssn = '9988776655'

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
#pilot1 = Pilot('1122334455','John', 'Captain', 'UPDATED', 'John@captain.com', 'UPDATED', '55874', 'FI-786')
#flight_attendant1 = Flight_Attendant('9988776655', 'Rose', 'Head flight attendant', 'wateveralane 89', 'rose@titanic.com', 'UPDATED', '88464')
#reg_upd_pilot = crew_class.register_updated_pilot_to_file(pilot1)
#reg_upd_flight_att = crew_class.register_updated_flight_attendant_to_file(flight_attendant)

voyage_class = Voyage_Data()

#a = datetime(2024, 1, 11, 8, 45)
#b = datetime(2023, 1, 11, 12, 30)
# departure_ice = datetime(2023,2,23,15,15,15)
# departure_dest = datetime(2023,2,23,20,20,20)
# the_voyage = Voyage('BAR_OLD', departure_ice, departure_dest, 'SOMETHING', 'SOMETHING')

# voyage_class.register_voyage_to_file(the_voyage)

# c = voyage_class.get_voyages_from_file()
# #d = voyage_class.get_voyage_from_file('Greenland', a)
# print(c[0].destination)
# #print(d.time_depart_destination)

#voyage_class.register_updated_voyage_to_file(the_voyage)

#get_voyages = voyage_class.get_voyages_from_file()
#for elm in get_voyages:
    #print(elm.destination, elm.time_depart_iceland, elm.time_depart_destination)

# desti = 'greenland_NEW'
# departure = datetime(2024, 1, 11, 8, 45)
# get_voyage = voyage_class.get_voyage_from_file(desti, departure)
# print(get_voyage.destination, get_voyage.time_depart_destination)

voyage_class.move_voyages_done_to_file()
