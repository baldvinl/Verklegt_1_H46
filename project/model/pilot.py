from model.crew import Crew

class Pilot(Crew):
    def __init__(self, ssn, name, job_title, address,
                 email, mobile_no, phone_no='', type_rating=''):
        super().__init__(ssn, name, address, job_title, email, mobile_no, phone_no)
        self.type_rating = type_rating