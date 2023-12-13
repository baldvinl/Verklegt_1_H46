class Voyage:
    def __init__(self, destination, time_depart_iceland, time_depart_destination,
                captain = '', pilot = '', head_flight_attendant = '', flight_attendant1 ='', flight_attendant2=''):
        self.destination = destination
        self.time_depart_iceland = time_depart_iceland
        self.time_depart_destination = time_depart_destination
        self.captain = captain
        self.pilot = pilot
        self.head_flight_attendant = head_flight_attendant
        self.flight_attendant1 = flight_attendant1
        self.flight_attendant2 = flight_attendant2


    def is_manned(self):
        """returns true if all captain pilot and head flight attendant are part of the crew"""
        return self.captain and self.pilot and self.head_flight_attendant