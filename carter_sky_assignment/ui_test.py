#
# STUDENTS NEED TO ADD CODE HERE
# Students need to add code in this module and change any functions as needed.
#

import ui


def test_print_menu():
    ui.print_menu()
    assert True


def test_print_banner():
    ui.print_banner()
    assert True


def test_input_menu_command(monkeypatch):

    for cmd in ui.MENU_CHOICE:
        # monkeypatch input() as if the user typed
        monkeypatch.setattr('builtins.input', lambda: cmd)

        cmd = ui.input_menu_command()
        assert cmd in ui.MENU_CHOICE
