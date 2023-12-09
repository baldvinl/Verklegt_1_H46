class Voyage:
    def __init__(self, destination='destination', time_depart_iceland = 'dd/mm/yy 00:00', time_depart_destination = 'dd/mm/yy 00:00', captain = '', pilot = '', head_flight_attendant = ''):
        self.destination = destination
        self.time_depart_iceland = time_depart_iceland
        self.time_depart_destination = time_depart_destination
        self.captain = captain 
        self.pilot = pilot
        self.head_flight_attendant = head_flight_attendant


    def is_manned(self):
        if self.captain and self.pilot and self.head_flight_attendant:
            return True
        else:
            return False