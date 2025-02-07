from os.path import commonpath

from _pytest._code import source


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

    def validate_name(self, name):
        if self.name.isalnum():
            return True
        else:
            return False

    def validate_comment(self, comment):
        if self.comment.isalnum():
            return True
        else:
            return False


    def validate_number(self, phone):

        if not ("+" and "(" and ")" and "-" in phone):
            return False

        if len(phone) > 0 and phone[0] == "+":
            phone = phone[1:]
        else:
            return False

        country_code = phone.split("(")

        if country_code[0].isdigit() and int(country_code[0]) > 0 and int(country_code[0]) < 1000:
            phone = phone[len(country_code[0]):]
        else:
            return False

        if phone[0] == "(":
            phone = phone[1:]
        else:
            return False

        region_code = phone.split(")")

        if region_code[0].isdigit() and int(region_code[0]) > 0 and int(region_code[0]) < 1000:
            phone = phone[len(region_code[0]):]
        else:
            return False

        if phone[0] == ")":
            phone = phone[1:]
        else:
            return False

        phone_number = phone.split("-")

        if (phone_number[0].isdigit() and
                len(phone_number[0]) == 3 and
                phone_number[1].isdigit() and
                len(phone_number[1]) == 2 and
                phone_number[2].isdigit() and
                len(phone_number[2]) == 2):
            return True
        else:
            return False

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
        return self.contacts

    def create_contact(self, name, phone, comment):
        contact_id = self.contacts[-1].contact_id + 1 if self.contacts else 1
        new_contact = Contact(contact_id, name, phone, comment)

        if (new_contact.validate_name(name) and
                new_contact.validate_comment(comment) and
                new_contact.validate_number(phone)):
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
                if field == "name" and contact.validate_name(new_value):
                    contact.name = new_value
                    return contact
                elif field == "phone" and contact.validate_number(new_value):
                    contact.phone = new_value
                    return contact
                elif field == "comment" and contact.validate_comment(new_value):
                    contact.comment = new_value
                    return contact
        return False

    def remove_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact.contact_id == contact_id:
                return self.contacts.pop(i)
        return None