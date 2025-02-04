
# class PhoneBook:
#     def __init__(self, path):
#         self.path = path
#
#     def get_contacts(self):
#         return open(self.path, "r", encoding="utf-8").read()
#
# pb = PhoneBook("./contacts.txt")
# print(pb.get_contacts())

class Read_File():
    def __init__(self, path):
        self.path = open(path, "r", encoding="utf-8").read()

read_file = Read_File("contacts.txt")
print(read_file.path)
