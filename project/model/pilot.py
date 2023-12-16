from model.crew import Crew

class Pilot(Crew):
    def __init__(self, ssn=None, name=None, job_title=None, address=None,
                email=None, mobile_no=None, phone_no='', type_rating=''):
        super().__init__(ssn, name, address, job_title, email, mobile_no, phone_no)
        self.type_rating = type_rating