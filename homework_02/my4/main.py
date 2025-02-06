
# class ReadFile():
#     def __init__(self, path, content):
#         self.path = path
#         self.content = content
#
#     def read_file(self):
#         try:
#             with open(self.path, "r", encoding="UTF-8") as file:
#                 content = file.read().strip().splitlines()
#                 return content
#         except FileNotFoundError:
#             print("file not found")
#
# class SaveFile:
#     def __init__(self, path, content):
#         self.path = path
#         self.content = content
#
#     def save_file(self):
#          with open(self.path, "w", encoding="UTF-8") as file:
#              return file.write("\n".join(self.content))


class PhoneBook:
    def __init__(self, path, content):
        self.path = path
        self.content = content


    def read_file(self):
        try:
            with open(self.path, "r", encoding="UTF-8") as file:
                content = file.read().strip().splitlines()
                return content
        except FileNotFoundError:
            print("file not found")

    def save_file(self):
        with open(self.path, "w", encoding="UTF-8") as file:
            return file.write("\n".join(self.content))

    def show_contacts(self):
        return "\n".join(str(i) for i in self.content)

    def _next_id(self):
        id = 1
        for i in range(1, len(self.content)):
            mylist = self.content[i].split()
            if int(mylist[0]) > id:
                id = int(mylist[0])
        return id +1
    def create_contact(self):
        name = input("Введите имя: ")
        phone = input("Введите номер: ")
        comment = input("Введите комментарий: ")
        new_contact = (str(self._next_id()) + " " +
                       name + " " +
                       phone + " " +
                       comment)
        self.content.append(new_contact)

if __name__ == '__main__':
    pb = PhoneBook("contacts.txt", [])
    pb.content = pb.read_file()

    pb.create_contact()
    pb.save_file()



    #pb2 = PhoneBook("contacts2.txt", [])
    #pb2.content = pb.content
    #pb2.save_file()