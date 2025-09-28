import command
import pyramid_tools
import ui
import video


def main():

    # clean temp video directory
    video.clean_temp_directory()

    # read pyramid.json
    pyramid = pyramid_tools.read()

    # start menu
    ui.print_banner()
    cmd = None
    while cmd != 'q':
        ui.print_menu()
        cmd = ui.input_menu_command()
        command.handle(pyramid, cmd)


main()
