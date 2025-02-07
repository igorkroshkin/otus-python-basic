from view import View
from model import Contact

"""
Тесты для класса View
"""
def test_view_menu_items(capsys):
    view = View()
    view.menu_items()
    captured = capsys.readouterr()
    assert "Программа телефонный справочник поддерживает следующие операции:" in captured.out

def test_view_show_contacts(capsys):
    view = View()
    contacts = [Contact(1, "Анатолий", "+7(999)101-11-12", "мобильный")]
    view.show_contacts(contacts)
    captured = capsys.readouterr()
    assert "1 Анатолий +7(999)101-11-12 мобильный" in captured.out

def test_view_show_message(capsys):
    view = View()
    view.show_message("Тестовое сообщение")
    captured = capsys.readouterr()
    assert "Тестовое сообщение" in captured.out