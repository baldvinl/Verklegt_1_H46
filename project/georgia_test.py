from model.crew import Crew
from model.pilot import Pilot
from model.flight_attendant import Flight_Attendant
from data.data_wrapper import Data_Wrapper
from logic.crew_logic import Crew_Logic
from logic.voyage_logic import Voyage_Logic
from pprint import pprint
from datetime import datetime, date, timedelta
from model.voyage import Voyage


wrapper = Data_Wrapper()
voyage_logic = Voyage_Logic(wrapper)
logic = Crew_Logic(wrapper, voyage_logic)

# test = Destination()
# logic.register_destination(test)
# datetimeinput = datetime.strptime("2023-05-11 08:45:00", "%Y-%m-%d %H:%M:%S")
# test = Voyage("GRE", datetimeinput, datetimeinput)
# list = voyage_logic.register_voyage(test)
#TypeError: 'str' object cannot be interpreted as an integer
# pprint(vars(list))
# member = Flight_Attendant("0210320392103", "sdklasflk", "flight attendant", "neverland", "absolutely@not.com", "0233495", "")
# member = logic.register_crew(member)
#pprint(vars(member))

# pilot1 = Pilot("skdmask", "askdjskd", "")
# pilot2 = Pilot()


# list = (pilot1, pilot2, ... )
lostofstuff = [1, 2, 3, 4]
for thing in lostofstuff:
    if thing == 5:
        return True
