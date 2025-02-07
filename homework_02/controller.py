import view
import model

class Controller:
    def __init__(self):
        self.phone_book = model.PhoneBook()
        self.view = view.View()

    def get_input(self, prompt):
        return input(prompt)

    def menu_open_file(self):
        self.phone_book.load_contacts()
        self.view.show_message("Файл успешно открыт.")

    def menu_save_file(self):
        self.phone_book.save_contacts()
        self.view.show_message("Файл успешно сохранен.")

    def menu_show_contacts(self):
        contacts = self.phone_book.show_contacts()
        self.view.show_message("Текущий список контактов: ")
        self.view.show_contacts(contacts)

    def menu_create_contact(self):
        name = self.get_input("Введите новое имя: ")
        phone = self.get_input("Введите новый телефонный номер: ")
        comment = self.get_input("Введите новый комментарий: ")

        new_contact = self.phone_book.create_contact(name, phone, comment)
        if new_contact:
            self.view.show_message(f"Контакт {new_contact.name} успешно создан.")
        else:
            self.view.show_message("Вы ввели недопустимые символы.")

    def menu_search_contact(self):
        self.menu_show_contacts()
        search_text = self.get_input("Введите строку для поиска: ")
        found_contacts = self.phone_book.find_contact(search_text)
        if found_contacts:
            self.view.show_message(f"Список контактов, удовлетворяющих условию \"{search_text}\":")
            self.view.show_contacts(found_contacts)
        else:
            self.view.show_message(f"Контактов, удовлетворяющих условию \"{search_text}\" не найдено.")

    def menu_modify_contact(self):
        self.menu_show_contacts()
        contact_id = self.get_input("Введите идентификатор контакта для изменения: ")

        modified_contact = ()
        contact_id_exist = False

        for contact in self.phone_book.contacts:
            if contact_id in str(contact.contact_id):
                contact_id_exist = True

        if contact_id_exist:
            field = self.get_input("Выберите поле для изменения ([1] - имя, [2] - телефон, [3] - комментарий): ")
            if field == "1":
                new_value = self.get_input("Введите новое имя: ")
                modified_contact = self.phone_book.modify_contact(int(contact_id), "name", new_value)
            elif field == "2":
                new_value = self.get_input("Введите новый номер: ")
                modified_contact = self.phone_book.modify_contact(int(contact_id), "phone", new_value)
            elif field == "3":
                new_value = self.get_input("Введите новый комментарий: ")
                modified_contact = self.phone_book.modify_contact(int(contact_id), "comment", new_value)

            if modified_contact:
                self.view.show_message(f"Контакт {modified_contact.name} успешно изменен.")
            else:
                self.view.show_message("Вы ввели недопустимые символы.")
        else:
            self.view.show_message(f"Контакта с идентификатором \"{contact_id}\" не найдено.")


    def menu_delete_contact(self):
        self.menu_show_contacts()
        contact_id = int(self.get_input("Введите идентификатор контакта для удаления: "))
        removed_contact = self.phone_book.remove_contact(contact_id)
        if removed_contact:
            self.view.show_message(f"Контакт {removed_contact.name} успешно удален.")
        else:
            self.view.show_message(f"Контакт с идентификатором \"{contact_id}\" не найден.")

    def menu_exit(self):
        exit()

    def run(self):
        while True:
            self.view.menu_items()
            operation = self.get_input("Введите номер операции: ")

            menu_actions = [
                self.menu_open_file,
                self.menu_save_file,
                self.menu_show_contacts,
                self.menu_create_contact,
                self.menu_search_contact,
                self.menu_modify_contact,
                self.menu_delete_contact,
                self.menu_exit,
            ]

            if operation.isdigit() and 1 <= int(operation) <= 8:
                menu_actions[int(operation) - 1]()
            else:
                self.view.show_message("Вы выбрали недопустимую операцию.")

            confirmation = self.get_input("Вы хотите продолжить? [Y/N, Д/Н]: ").lower()
            if confirmation in ["n", "н"]:
                break
