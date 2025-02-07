import pytest

"""
Фикстура для временного файла контактов
"""
@pytest.fixture
def temp_contacts_file():
    file_path = "test_contacts.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Идентификатор Имя Телефон Комментарий\n")
        file.write("1 Анатолий +7(999)101-11-12 мобильный\n")
        file.write("2 Мария +49(500)234-56-90 рабочий\n")
    return file_path
