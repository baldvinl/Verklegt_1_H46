from project.model.crew import Crew

class Pilot(Crew):
    def __init__(self, ssn='9999999999', name='Chuck Norris', address='Beststreet 1', area_code='999', 
                 email='chucknorris@ru.is', mobile_no='9999999', phone_no='', type_rating='xxxx'):
        super().__init__(ssn, name, address, area_code, email, mobile_no, phone_no)
        self.type_rating = type_rating