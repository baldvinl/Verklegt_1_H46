
from ui.ui_menu_display import Main_Menu
from ui.ui_menu_display import Header_Footer
from ui.ui_menu_display import Inputs_Prompt
from ui.ui_menu_display import Employee_Menu


from ui.ui_validation import Validation_Ui
test_validation = Validation_Ui("1234567890", "John Doe", "123-456-7890", "123 Main St")
test_validation.validate_ssn('932k32')

# test_header = Header_Footer()
# test_input = Inputs_Prompt()
# test_main = Main_Menu()
# test_employee = Employee_Menu()
# reg_captain = Employee_Menu()


# test_header.display_main_header()
# test_header.lines_above_in_submenu()
# test_employee.register_head_flight_attentant()
# test_header.display_main_footer_with_q_m_b()
# test_input.menu_number()

# test_header.display_main_header()
# test_header.lines_above_in_submenu()
# test_main.display_main_menu()
# test_header.display_main_footer_with_q_m_b()
# test_input.menu_number()

# test_header.display_main_header()
# test_header.lines_above_in_submenu()
# test_employee.display_employees_menu()
# test_header.display_main_footer_with_q_m_b()
# test_input.menu_number()