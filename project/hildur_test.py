from ui.validation__ui import Validation_Ui
from ui.print_lists_ui import List_Print_UI
from model.pilot import Pilot



test_list = List_Print_UI(
    "9392929392",
    "Hildur",
    "Kennari",
    "Arkarvogi 2",
    "hildur@ru.is",
    "83828383",
    "94993939",
    "FF-FFR",
    'logic'
)

# test_list.display_list('9393929292', 'Adalsteinn', 'Pilot', 'Markarflot 20', 'addi.gisla@gmail.com', '49494949', '4939393', 'kdk')
pilot1 = Pilot('9393929292', 'Adalsteinn Gíslason',  'Markarflot 20', 'H. f. attentant', 'addi.gisla@gmail.com', '49494949', '4939393', 'kdk')
pilot2 = Pilot('9393929292', 'Adalsteinn Gísalson',  'Markarflot 20','Pilot', 'addi.gisla@gmail.com', '49494949', '4939393', 'kdk')

a_list = (pilot1, pilot2)

test_list.display_list(a_list)


# test_val = Validation_Ui(
#     "no symbols",
#     "number",
#     "letters",
#     "0203459939",
#     "Addi",
#     "858383",
#     "Dufnaholar 10",
#     "hildur@ru.is",
#     "KEF",
#     "03:59",
#     "453",
#     "kdkd",
#     "empty",
#     "wrapper"
# )
# test_val.display_list()
# test_val.validate_no_punctuation("k66$kd")
# test_val.validate_no_numbers("le1tt$ers")
# test_val.validate_no_letter('393$93')
# test_val.validate_ssn("1234567890888")
# test_val.validate_name_and_country("Aslei")
# test_val.validate_phone_number("9494%944")
# test_val.validate_address("Ksljflsaieugæ")
# test_val.validate_airport('K&F')
# test_val.validate_email('hildur@ru.is')
# test_val.validate_flight_time("121d")
# test_val.validate_distance('444')
