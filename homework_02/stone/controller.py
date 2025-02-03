import text
import view
from model import PhoneBook


class Controller:
    def __init__(self, path: str):
        self.pb: PhoneBook = PhoneBook(path)

    def open_file(self):
        self.pb.read_file()
        view.message(text.open_file_successful)

    def save_file(self):
        self.pb.save_file()
        view.message(text.save_file_successful)

    def show_all_contacts(self):
        view.show_contacts(
            self.pb.phonebook,
            text.empty_phone_book,
        )

    def create_contact(self):
        new_contact = view.input_data(text.create_new_user)
        self.pb.create_contact(new_contact)
        view.message(text.contact_create_successful.format(name=new_contact[0]))

    def find_contact(self):
        key_word = view.input_data(text.input_key_word_to_find, single=True)
        search_result = self.pb.find_contact(key_word)
        view.show_contacts(search_result, text.null_search_result.format(key_word=key_word))

    def edit_contact(self):
        id_to_edit = view.input_data(text.input_id_to_edit, single=True)
        new_contact = view.input_data(text.edit_user)
        name_edit_contact = self.pb.edit_contact(id_to_edit, new_contact)
        view.message(text.edit_contact_successful.format(name=name_edit_contact))

    def delete_contact(self):
        id_to_delete = view.input_data(text.input_id_to_delete, single=True)
        contact_name = self.pb.delete_contact(id_to_delete)
        view.message(text.contact_delete_successful.format(name=contact_name))

    def end_work(self):
        exit()


def start_app():
    main_ctrl = Controller('phone_book.txt')
    while True:
        view.show_main_menu()
        user_choice = view.main_menu_user_choice()

        main_menu_controller = [
            main_ctrl.open_file,
            main_ctrl.save_file,
            main_ctrl.show_all_contacts,
            main_ctrl.create_contact,
            main_ctrl.find_contact,
            main_ctrl.edit_contact,
            main_ctrl.delete_contact,
            main_ctrl.end_work,
        ]
        main_menu_controller[user_choice - 1]()
