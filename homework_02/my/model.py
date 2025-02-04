class PhoneBook:
    """
    класс хранит текущий список контактов и манипулирует ими
    """
    pass

class Contact:
    """
    класс хранит данные контакта и манипулирует ими
    """
    pass

class ReadFile:
    """
    класс для чтения данных из файла
    """
    def __init__(self, path):
        self.path = open(path, "r", encoding="utf-8").read()

class WriteFile:
    """
    класс для записи данных в файл
    """
    def __init__(self, path):
        self.path = open(path, "w", encoding="utf-8").write()
