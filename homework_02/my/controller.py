import model
import view

class Controller:

    def __init__(self, path):
        self.path = path

    def open_file(self):
        pass

    def exit_app(self):
        pass


def start_app():

    controller = Controller()

    user_selector = [
        controller.open_file,
        controller.exit_app
    ]

    user_selector[view.user_menu_item-1]()



