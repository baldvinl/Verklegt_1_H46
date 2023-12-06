from project.model.crew import Crew


class Flight_Attendant(Crew):
    def __init__(self, ssn='9999999999', name='Chuck Norris', address='Beststreet 1', 
                 area_code='999', email='chucknorris@ru.is', mobile_no='9999999', phone_no=None):
        super().__init__(ssn='9999999999', name='Chuck Norris', address='Beststreet 1', 
                         area_code='999', email='chucknorris@ru.is', mobile_no='9999999', phone_no=None)