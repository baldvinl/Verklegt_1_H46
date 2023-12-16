class Crew:
    def __init__(self, ssn=None, name=None, job_title=None, address=None, email=None, mobile_no=None, phone_no=''):
        self.ssn = ssn
        self.name = name
        self.job_title = job_title
        self.address = address
        self.email = email
        self.mobile_no = mobile_no
        self.phone_no = phone_no 

    def attribute_implementation(self, attributes_list):
        self.address = attributes_list[0]
        self.email = attributes_list[1]
        self.mobile_no = attributes_list[2]
        self.phone_no = attributes_list[3]