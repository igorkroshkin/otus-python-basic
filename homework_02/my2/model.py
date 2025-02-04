
class PhoneBook:
    def __init__(self, path):
        self.path = path

    def open_file(self):
        return open(self.path, "r", encoding="utf-8").read()

    def save_file(self):
        return open(self.path, "w", encoding="utf-8").write(self.open_file())


# class ReadFile:
#     """
#     класс для чтения данных из файла
#     """
#     def __init__(self, path):
#         self.path = open(path, "r", encoding="utf-8").read()
#
# class WriteFile:
#     """
#     класс для записи данных в файл
#     """
#     def __init__(self, path):
#         self.path = open(path, "w", encoding="utf-8").write()