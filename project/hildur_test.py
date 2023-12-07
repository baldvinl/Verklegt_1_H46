from ui.ui_menu_display import Main_Menu
from ui.ui_menu_display import Header_Footer
from ui.ui_menu_display import Inputs_Prompt


test_header = Header_Footer()
test_menu = Main_Menu()
test_input = Inputs_Prompt()

test_header.get_main_header()
test_menu.get_main_menu()
test_header.get_main_footer_with_q_m()
test_input.menu_number()