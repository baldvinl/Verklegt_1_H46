from model.aircraft import Aircraft
from data.data_wrapper import Data_Wrapper
from logic.aircraft_logic import *

wrapper = Data_Wrapper()
logic = Aircraft_Logic(wrapper)

aicraftA = Aircraft("blabla", "lsdkals", "masdasjd", 30)
logic.get_aircraft_info("blabla")