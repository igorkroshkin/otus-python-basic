class View:
    def menu_items(self):
        print("Программа телефонный справочник поддерживает следующие операции:")
        print("[1] - открыть файл")
        print("[2] - сохранить файл")
        print("[3] - показать все контакты")
        print("[4] - создать контакт")
        print("[5] - найти контакт")
        print("[6] - изменить контакт")
        print("[7] - удалить контакт")
        print("[8] - выход")

    def show_contacts(self, contacts):
        for contact in contacts:
            print(contact)

    def show_message(self, message):
        print(message)