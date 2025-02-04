import view
import model

class Controller:

    def __init__(self, pb: model.PhoneBook):
        self.pb = pb
    def open_file(self):
        pb.open_file()
    def save_file(self):
        pass
    def exit_app(self):
        pass
def start_app():

    controller = Controller()

    view.show_menu_items()

    user_choice_input = input("Выберите пункт меню: ")

    menu_items = [
        controller.open_file,
        controller.save_file,
        controller.exit_app
    ]

    menu_items[user_choice_input - 1]()
