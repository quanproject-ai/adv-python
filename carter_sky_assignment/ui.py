#
# STUDENTS NEED TO ADD CODE HERE
# Students need to add code in this module and change any functions as needed.
#

# menu constants
MENU_CHOICE = {
    'p': {
        'name': 'Print',
        'description': 'Print the pyramid'
    },
    'q': {
        'name': 'Quit',
        'description': 'Quit'
    },
}


def print_banner():
    print()


def print_menu():
    print('commands:')
    for cmd in MENU_CHOICE:
        print(f'\t{cmd}')
    print()


def input_menu_command():
    is_cmd = False
    while not is_cmd:
        print('Enter a command: ', end='')
        cmd = input()
        if cmd in MENU_CHOICE:
            is_cmd = True
        else:
            print(f'ERROR: \'{cmd}\' is not a valid command')
            print()
            cmd = None
    return cmd
