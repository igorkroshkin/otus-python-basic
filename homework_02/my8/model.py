class ReadFile:
    @staticmethod
    def read():
        contacts = []
        with open("contacts.txt", "r", encoding="utf-8") as file:
            next(file)  # Skip header
            for line in file:
                contact_id, name, phone, comment = line.strip().split(maxsplit=3)
                contacts.append(Contact(int(contact_id), name, phone, comment))
        return contacts

class SaveFile:
    @staticmethod
    def save(contacts):
        with open("contacts.txt", "w", encoding="utf-8") as file:
            file.write("Идентификатор Имя Телефон Комментарий\n")
            for contact in contacts:
                file.write(f"{contact}\n")

class Contact:
    def __init__(self, contact_id, name, phone, comment):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f"{self.contact_id} {self.name} {self.phone} {self.comment}"

class PhoneBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        self.contacts = ReadFile.read()

    def save_contacts(self):
        SaveFile.save(self.contacts)

    def show_contacts(self):
        for contact in self.contacts:
            print(contact)

    def create_contact(self, name, phone, comment):
        contact_id = self.contacts[-1].contact_id + 1 if self.contacts else 1
        new_contact = Contact(contact_id, name, phone, comment)
        self.contacts.append(new_contact)
        return new_contact

    def find_contact(self, search_text):
        found = []
        for contact in self.contacts:
            if (search_text in str(contact.contact_id) or
                search_text in contact.name or
                search_text in contact.phone or
                search_text in contact.comment):
                found.append(contact)
        return found

    def modify_contact(self, contact_id, field, new_value):
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                if field == "name":
                    contact.name = new_value
                elif field == "phone":
                    contact.phone = new_value
                elif field == "comment":
                    contact.comment = new_value
                return contact
        return None

    def remove_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact.contact_id == contact_id:
                return self.contacts.pop(i)
        return None