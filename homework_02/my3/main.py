import messages
class ReadFile:

    def __init__(self, path):
        self.path = path

    def read_file(self):
        try:
            with open(self.path, "r", encoding="UTF-8") as file:
                return file.read().strip().splitlines()
        except FileNotFoundError:
            print(messages.file_not_found)
class SaveFile:
    def __init__(self, path, content):
        self.path = path
        self.content = content

    def save_file(self):
         with open(self.path, "w", encoding="UTF-8") as file:
             return file.write("\n".join(self.content))


class PhoneBook():
    def __init__(self, content: list):
        self.content = content

    def show_contacts(self) -> str:
        return "\n".join(str(i) for i in self.content)



class Contact:
    pass

class Menu:
    def show_menu():
        s = "\n".join(messages.menu_items)
        print(s)

if __name__ == '__main__':

    pb = PhoneBook

    Menu.show_menu()
    while True:

        # условие выхода из цикла меню
        condition = 0

        operation = input(messages.menu_item_choice)

        if operation == "1":
            pb.content = ReadFile("contacts.txt").read_file()
            if pb.content:
                print(messages.file_opened_success)
        elif operation == "2":
            if pb.content:
                SaveFile("contacts.txt", pb.content).save_file()
                print(messages.file_saved_success)
            else:
                print(messages.file_not_opened)
        elif operation == "3":
            if pb.content:
                print(pb.show_contacts(pb))
            else:
                print(messages.file_not_opened)
        elif operation == "4":
            create_contact()
        elif operation == "5":
            find_operation = input(
                "Выберите по каким полям будет осуществляться поиск, [1] - по всем полям, [2] - по идентификатору, [3] - по имени, [4] - по номеру телефона, [5] - по комментарию: ")
            if find_operation == "1":
                find_contact()
            elif find_operation == "2":
                find_contact_by_id()
            elif find_operation == "3":
                find_contact_by_name()
            elif find_operation == "4":
                find_contact_by_number()
            elif find_operation == "5":
                find_contact_by_comment()
            else:
                print("Вы ввели недопустимый символ!")
        elif operation == "6":
            modify_contact()
        elif operation == "7":
            remove_contact()
        elif operation == "8":
            break
        else:
            print("Вы ввели недопустимый символ!")

        # цикл подтверждения
        while True:

            confirmation = input("Вы хотите продолжить? [Y/N, Д/Н]: ").lower()

            if confirmation in ["y", "д"]:
                #menu_items()
                Menu.show_menu()
                condition = 1
                break
            elif confirmation in ["n", "н"]:
                break
            else:
                print("Вы ввели недопустимый символ!")
                continue

        if condition:
            continue
        else:
            break


