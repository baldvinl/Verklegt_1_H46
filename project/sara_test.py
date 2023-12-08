from ui.ui_menu_display import Main_Menu
from ui.ui_menu_display import Crew_Menu
from ui.ui_menu_display import Destination_Menu
from ui.ui_menu_display import Voyages_Menu
from ui.ui_menu_display import Aircraft_Menu
from ui.ui_menu_display import Print_Menu
from ui.ui_menu_display import Header_Footer
from ui.ui_menu_display import Inputs_Prompt


test_header = Header_Footer()
# test_menu = Main_Menu()
# test_cmenu = Crew_Menu()
# test_dmenu = Destination_Menu()
# test_vmenu = Voyages_Menu()
# test_amenu = Aircraft_Menu()
test_pmenu = Print_Menu()
test_input = Inputs_Prompt()

test_header.get_main_header()
# test_menu.get_main_menu()
# test_cmenu.get_crew_menu()
# test_dmenu.get_destination_menu()
# test_vmenu.get_voyage_menu()
# test_amenu.get_aircraft_menu()
test_pmenu.get_print_menu()
test_header.get_main_footer_with_q_m_b()
test_input.menu_number()