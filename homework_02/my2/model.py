
class PhoneBook:
    def __init__(self, path):
        self.path = path

    def open_file(self):
        return open(path, "r", encoding="utf-8").read()