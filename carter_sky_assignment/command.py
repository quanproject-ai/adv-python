#
# STUDENTS NEED TO ADD CODE HERE
# Students need to add code in this module and change any functions as needed.
#

# STUDENTS WILL PROBAbLY NEED TO IMPORT THESE TWO MODULES
# import config
# import video


from config import logger


def handle_print(pyramid):
    print()
    print('print a pyramid')
    print()


def handle(pyramid, cmd):
    if cmd == 'p':
        handle_print(pyramid)
    elif cmd == 'q':
        return
    else:
        logger.error('ERROR: command not implemented')
