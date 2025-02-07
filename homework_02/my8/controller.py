

def run(self):
    while True:
        self.menu_items()
        operation = input("Введите номер операции: ")
        if operation == "1":
            self.phone_book.load_contacts()
            print("Файл успешно открыт.")
        elif operation == "2":
            self.phone_book.save_contacts()
            print("Файл успешно сохранен.")
        elif operation == "3":
            self.phone_book.show_contacts()
        elif operation == "4":
            name = input("Введите новое имя: ")
            phone = input("Введите новый телефонный номер: ")
            comment = input("Введите новый комментарий: ")
            new_contact = self.phone_book.create_contact(name, phone, comment)
            print(f"Контакт {new_contact.name} успешно создан.")
        elif operation == "5":
            search_text = input("Введите строку для поиска: ")
            found_contacts = self.phone_book.find_contact(search_text)
            if found_contacts:
                for contact in found_contacts:
                    print(contact)
            else:
                print("Контактов не найдено.")
        elif operation == "6":
            contact_id = int(input("Введите идентификатор контакта для изменения: "))
            field = input("Выберите поле для изменения (name, phone, comment): ")
            new_value = input("Введите новое значение: ")
            modified_contact = self.phone_book.modify_contact(contact_id, field, new_value)
            if modified_contact:
                print(f"Контакт {modified_contact.name} успешно изменен.")
            else:
                print("Контакт не найден.")
        elif operation == "7":
            contact_id = int(input("Введите идентификатор контакта для удаления: "))
            removed_contact = self.phone_book.remove_contact(contact_id)
            if removed_contact:
                print(f"Контакт {removed_contact.name} успешно удален.")
            else:
                print("Контакт не найден.")
        elif operation == "8":
            break
        else:
            print("Недопустимая операция.")

        confirmation = input("Вы хотите продолжить? [Y/N, Д/Н]: ").lower()
        if confirmation in ["n", "н"]:
            break