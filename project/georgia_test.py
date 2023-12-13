from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant
from data.data_wrapper import Data_Wrapper
from logic.crew_logic import Crew_Logic
from logic.voyage_logic import Voyage_Logic
from pprint import pprint
from logic.validation_check import ValidationLogic
from datetime import datetime
from model.voyage import Voyage


wrapper = Data_Wrapper()
voyage_logic = Voyage_Logic(wrapper)
validator = ValidationLogic(wrapper)
logic = Crew_Logic(wrapper, voyage_logic)

# test = Destination()
# logic.register_destination(test)
datetimeinput = datetime.strptime("2023-05-11 08:45:00", "%Y-%m-%d %H:%M:%S")
test = Voyage("GRE", datetimeinput, datetimeinput)
list = voyage_logic.register_voyage(test)
# pprint(vars(list))
print(list)