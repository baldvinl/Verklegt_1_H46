from ui.ui_validation import Validation_Ui

test_val = Validation_Ui(
    "no symbols",
    "number",
    "letters",
    "0203459939",
    "Addi",
    "858383",
    "Dufnaholar 10",
    "hildur@ru.is",
    "KEF",
    "03:59",
    "453",
    "kdkd"
)
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
test_val.validate_aircraft_name('K2-DDD')
