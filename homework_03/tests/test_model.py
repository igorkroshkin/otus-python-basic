from model import ReadFile, SaveFile, Contact, PhoneBook

"""
Тесты для класса ReadFile
"""
def test_readfile_read(temp_contacts_file):
    contacts = ReadFile.read()
    assert contacts[0].name == "Анатолий"

"""
Тесты для класса SaveFile
"""
def test_savefile_save(temp_contacts_file):
    contacts = [Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")]
    SaveFile.save(contacts)
    with open(temp_contacts_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert lines[1].strip() == "1 Анатолий +7(999)101-11-12 мобильный"

""" 
Тесты для класса Contact
"""
def test_contact_creation():
    contact = Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")
    assert contact.contact_id == 1
    assert contact.name == "Анатолий"
    assert contact.phone == "+7(999)101-11-12"
    assert contact.comment == "мобильный"

def test_contact_str():
    contact = Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")
    assert str(contact) == "1 Анатолий +7(999)101-11-12 мобильный"

"""
Тесты для класса PhoneBook
"""
def test_phonebook_load_contacts(temp_contacts_file):
    phone_book = PhoneBook()
    phone_book.contacts = []  # Очищаем контакты перед загрузкой
    phone_book.load_contacts()
    assert phone_book.contacts[0].name == "Анатолий"

def test_phonebook_save_contacts(temp_contacts_file):
    phone_book = PhoneBook()
    phone_book.contacts = [Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")]
    phone_book.save_contacts()
    with open(temp_contacts_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert lines[1].strip() == "1 Анатолий +7(999)101-11-12 мобильный"

def test_phonebook_create_contact():
    phone_book = PhoneBook()
    phone_book.contacts = []
    new_contact = phone_book.create_contact("Анатолий", "+7(999)101-11-12", "мобильный")
    assert new_contact.contact_id == 1
    assert new_contact.name == "Анатолий"
    assert len(phone_book.contacts) == 1

def test_phonebook_find_contact():
    phone_book = PhoneBook()
    phone_book.contacts = [
        Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный"),
    ]
    found_contacts = phone_book.find_contact(search_field="2", search_text="Анатолий")
    assert len(found_contacts) == 1
    assert found_contacts[0].name == "Анатолий"

def test_phonebook_modify_contact():
    phone_book = PhoneBook()
    phone_book.contacts = [Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")]
    modified_contact = phone_book.modify_contact(1, "name", "Антон")
    assert modified_contact.name == "Антон"

def test_phonebook_remove_contact():
    phone_book = PhoneBook()
    phone_book.contacts = [Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")]
    removed_contact = phone_book.remove_contact(1)
    assert removed_contact.name == "Анатолий"
    assert len(phone_book.contacts) == 0