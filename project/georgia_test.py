from model.aircraft import Aircraft
from data.data_wrapper import Data_Wrapper
from logic.destination_logic import *
from pprint import pprint
from logic.validation_check import ValidationLogic


wrapper = Data_Wrapper()
validator = ValidationLogic(wrapper)
logic = Destination_Logic(wrapper, validator)

test = Destination("OOG", "dlskfj", "03:00", "300", "test", "04359034")
logic.register_destination(test)
# pprint(vars(list))