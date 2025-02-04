import view
import model
import messages

class Controller:

    def __init__(self, pb: model.PhoneBook):
        self.pb = pb
    def open_file(self):
        self.pb.open_file()
        view.print_message(messages.file_opened_successfully)
    def save_file(self):
        self.pb.save_file()
        view.print_message(messages.file_saved_successfully)

    def show_contacts(self):
        pass

    def exit_app(self):
        pass
def start_app():

    controller = Controller(model.PhoneBook("contacts.txt"))

    view.show_menu_items()

    user_choice_input = int(input("Выберите пункт меню: "))

    menu_items = [
        controller.open_file,
        controller.save_file,
        controller.exit_app
    ]

    menu_items[user_choice_input - 1]()
