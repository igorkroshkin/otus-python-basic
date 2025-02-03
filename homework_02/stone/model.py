

class PhoneBook:
    def __init__(self, path: str, separator: str = ';'):
        self.path = path
        self.separator = separator
        self.phonebook = {}

    def read_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            self.phonebook = {i: row.strip().split(self.separator) for i, row in
                              enumerate(file.readlines(), 1)}

    def save_file(self):
        data = '\n'.join([self.separator.join(contact) for contact in self.phonebook.values()])
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def _next_id(self):
        if self.phonebook:
            return max(self.phonebook) + 1
        return 1

    def create_contact(self, new_contact: list[str]):
        cur_id = self._next_id()
        self.phonebook[cur_id] = new_contact

    def find_contact(self, key_word: str):
        search_result = {}
        for i, contact in self.phonebook.items():
            for field in contact:
                if key_word.lower() in field.lower():
                    search_result[i] = contact
                    break
        return search_result

    def edit_contact(self, id_to_edit: str, new_contact: list[str]) -> str:
        current_contact = self.phonebook[int(id_to_edit)]
        for i in range(len(current_contact)):
            current_contact[i] = new_contact[i] if new_contact[i] else current_contact[i]
        self.phonebook[int(id_to_edit)] = current_contact
        return current_contact[0]

    def delete_contact(self, id_to_delete: str):
        contact = self.phonebook.pop(int(id_to_delete))
        return contact[0]
