from controller import Controller
import pytest

"""
Тесты для класса Controller
"""
def test_controller_get_input(monkeypatch):
    controller = Controller()
    monkeypatch.setattr("builtins.input", lambda _: "test input")
    assert controller.get_input("Введите что-нибудь: ") == "test input"

def test_controller_run(monkeypatch, capsys):
    controller = Controller()

    # Эмулируем ввод пользователя: открыть файл, показать контакты, выйти
    inputs = ["1", "Y", "3", "Y", "8"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    # Ожидаем завершение программы с SystemExit()
    with pytest.raises(SystemExit):
        controller.run()

    captured = capsys.readouterr()
    assert "Файл успешно открыт" in captured.out
    assert "1 Анатолий +7(999)101-11-12 мобильный" in captured.out
    assert "Выход из программы телефонный справочник!" in captured.out