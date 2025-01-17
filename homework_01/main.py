### Программа телефонный справочник
### homework_01, курс Otus-Python-Basic
### Автор Крошкин Игорь, 17.01.2025

FILE = "contacts.txt" # содержит список контактов
COLUMNS = 4 # количество столбцов в файле контактов

### [0] - вывод  меню
def menu_items():
    print("Программа телефонный справочник поддерживает следующие операции:")
    print("[1] - открыть файл")
    print("[2] - сохранить файл")
    print("[3] - показать все контакты")
    print("[4] - создать контакт")
    print("[5] - найти контакт")
    print("[6] - изменить контакт")
    print("[7] - удалить контакт")
    print("[8] - выход")

### [1] - открыть файл
def open_file():
    return open(FILE, "r", encoding = "utf-8")

### [2] - сохранить файл
def save_file(data: str):
    content = open_file().read()

    if data == content:
        print("Текущий список контактов совпадает со списком в файле, поэтому данные не будут перезаписаны.")
    else:
        with open(FILE, "w", encoding = "utf-8") as file:
            file.write(data)
            print(f"Текущий список контактов успешно сохранен в файл \"{FILE}\"")

### [3] - вывод на экран списка контактов из буфера
def show_contacts():
    global buffer
    print("Текущий список контактов:")
    print(buffer)
    return buffer

### [4] добавление нового контакта в буфер, идентификатор задается автоматически
def create_contact():
    global buffer

    content_list = str_to_list(buffer)

    contact_name = input("Введите новое имя. Поддерживаются только буквы и цифры : ")

    if not if_valid_name_comment(contact_name):
        print(f"Введенное имя \"{contact_name}\" содержит недопустимые символы.")
    else:
        contact_phone = input("Введите новый телефонный номер в международном формате, например, +7(123)456-78-90: ")
        if not if_valid_number(contact_phone):
            print(f"Введенный номер телефона \"{contact_phone}\" содержит недопустимые символы.")
        else:
            contact_comment = input("Введите новый комментарий. Поддерживаются только буквы и цифры : ")
            if not if_valid_name_comment(contact_comment):
                print(f"Введенный комментарий \"{contact_comment}\" содержит недопустимые символы.")
            else:
                contact_id = int(content_list[len(content_list) - 1][0]) + 1
                buffer += "\n" + \
                          str(contact_id) + " " + \
                          contact_name + " " + \
                          contact_phone + " " + \
                          contact_comment
                print(f"Контакт \"{contact_name}\" с идентификатором \"{contact_id}\" успешно создан.")

### [5] - найти контакт в буфере
def find_contact():
    global buffer

    found = []

    # строка для поиска
    show_contacts()
    content = str_to_list(buffer)
    find_text = input("Поиск осуществляется по следующим полям: Идентификатор, Имя, Телефон, Комментарий. Введите строку для поиска: ")

    # поиск совпадений
    for i in range(0, len(content)):
        for j in range(0, COLUMNS):
            if find_text in content[i][j]:
                found.append(content[i])

    # печать совпадений
    if len(found) > 0:
        print(f"Список контактов, удовлетворяющих строке поиска \"{find_text}\":")
        for i in range(0, len(found)):
            str = ""
            for j in range(0, COLUMNS):
                str += found[i][j] + " "
            print(str)
    else:
        print(f"Контактов, удовлетворяющих строке поиска \"{find_text}\" не найдено.")

### [6] - изменить контакт в буфере на основе идентификатора
def modify_contact():
    global buffer

    show_contacts()
    content = str_to_list(buffer)

    modify_id = int(input("Введите идентификатор контакта для изменения: "))

    index = 0

    # определение индекса контакта для изменения
    for i in range(1, len(content)):
        if modify_id == int(content[i][0]):
            index = i

    #  изменение контакта с валидацией введенных значений
    if index > 0:
        modify_field = input("Выберите поле для изменения, где [1] - Имя, [2] - Телефон, [3] - Комментарий: ")
        if modify_field == "1":
            modify_name = input("Введите новое имя: ")
            if if_valid_name_comment(modify_name):
                print(f"Имя \"{content[index][1]}\" успешно изменено на \"{modify_name}\".")
                content[index][1] = modify_name
            else:
                print("Вы ввели недопустимое имя. Поддерживаются только буквы и цифры.")
        elif modify_field == "2":
            modify_number = input("Введите новый номер телефона: ")
            if if_valid_number(modify_number):
                print(f"Номер телефона \"{content[index][2]}\" успешно изменен на \"{modify_number}\".")
                content[index][2] = modify_number
            else:
                print("Вы ввели недопустимый формат для международного номера телефона. Поддерживаемый формат: +7(123)456-78-90.")
        elif modify_field == "3":
            modify_comment = input("Введите новый комментарий: ")
            if if_valid_name_comment(modify_comment):
                print(f"Комментарий \"{content[index][3]}\" успешно изменен на \"{modify_comment}\".")
                content[index][3] = modify_comment
            else:
                print("Вы ввели недопустимый комментарий. Поддерживаются только буквы и цифры.")
        else:
            print("Вы ввели недопустимое значение поля для изменений.")
    else:
        print("Такого идентификатора не существует")

    buffer = list_to_str(content)[:-2]

### [7] - удалить контакт из буфера на основе идентификатора
def remove_contact():
    global buffer

    show_contacts()
    content = str_to_list(buffer)

    number = int(input("Введите идентификатор контакта для удаления: "))

    index = 0

    for i in range(1, len(content)):
        if number == int(content[i][0]):
            index = i

    if index > 0:
        print(f"Контакт \"{content[index][1]}\" с идентификатором \"{content[index][0]}\" успешно удален.")
        content.pop(index)
    else:
        print(f"Идентификатора с номером  \"{number}\" не существует")

    buffer = list_to_str(content)[:-2]

### преобразование списка в строку, используется при работе с буфером
def str_to_list(data: str):
    return [line.split() for line in data.splitlines()]

### преобразование строки в список, используется при работе с буфером
def list_to_str(data: list):
    content_str = ""
    for i in range(len(data)):
        for j in range(COLUMNS):
            content_str += data[i][j] + " "
        content_str += "\n"
    return content_str

### распознавание имени и комментария, поддерживаются только буквы и цифры
def if_valid_name_comment(data: str):
    if data.isalnum():
        return True
    else:
        return False

### распознавание номера телефона, поддерживается только международный формат, например: +7(123)456-78-90
def if_valid_number(data: str):

    if not ("+" and "(" and ")" and "-" in data):
        return False

    if len(data) > 0 and data[0] == "+":
        data = data[1:]
    else:
        return False

    country_code = data.split("(")

    if country_code[0].isdigit() and int(country_code[0]) > 0 and int(country_code[0]) < 1000:
        data = data[len(country_code[0]):]
    else:
        return False

    if data[0] == "(":
        data = data[1:]
    else:
        return False

    region_code = data.split(")")

    if region_code[0].isdigit() and int(region_code[0]) > 0 and int(region_code[0]) < 1000:
        data = data[len(region_code[0]):]
    else:
        return False

    if data[0] == ")":
        data = data[1:]
    else:
        return False

    phone_number = data.split("-")

    if (phone_number[0].isdigit() and
            len(phone_number[0]) == 3 and
            phone_number[1].isdigit() and
            len(phone_number[1]) == 2 and
            phone_number[2].isdigit() and
            len(phone_number[2]) == 2):
        return True
    else:
        return False

### основная функция
if __name__ == "__main__":

    buffer = open_file().read()

    menu_items()

    while True:

        # условие выхода из цикла меню
        condition = 0

        operation = input("Введите номер операции: ")

        if operation == "1":
            print(f"Файл \"{FILE}\" успешно открыт.")
            open_file()
        elif operation == "2":
            save_file(buffer)
        elif operation == "3":
            show_contacts()
        elif operation == "4":
            create_contact()
        elif operation == "5":
            find_contact()
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
                menu_items()
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