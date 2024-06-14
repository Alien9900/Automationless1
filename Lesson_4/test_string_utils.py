import pytest
from string_utils import StringUtils

# Создаем экземпляр класса StringUtils для использования в тестах
utils = StringUtils()

def test_capitalize():
    # Позитивный тест
    assert utils.capitilize("universe") == "Universe"
    # Негативный тест
    assert utils.capitilize("Universe") != "universe"

def test_trim():
    # Позитивный тест
    assert utils.trim("   Emirates") == "Emirates"
    # Негативный тест
    assert utils.trim("emirates   ") == "emirates   "  # Ожидаем, что пробелы в конце строки не удаляются


def test_to_list():
    # Позитивный тест
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    # Негативный тест
    assert utils.to_list("", ":") == []

def test_contains():
    # Позитивный тест
    assert utils.contains("Tatinomi", "t") is True
    # Негативный тест
    assert utils.contains("Tatinomi", "Z") is False

def test_delete_symbol():
    # Позитивный тест
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    # Негативный тест
    assert utils.delete_symbol("SkyPro", "x") == "SkyPro"  # Символа x нет в строке, строка остается неизменной

def test_starts_with():
    # Позитивный тест
    assert utils.starts_with("Ulandy", "U") is True
    # Негативный тест
    assert utils.starts_with("Ulandy", "A") is False

def test_end_with():
    assert utils.end_with("Marvel", "l") is True
    assert utils.end_with("Marvel", "m") is False
    # Негативный тест: передаем пустую строку
    assert utils.end_with("", "o") is False, "Пустая строка не должна заканчиваться на 'o'"

def test_is_empty():
    # Позитивные тесты
    assert utils.is_empty("") is True, "Пустая строка должна возвращать True"
    assert utils.is_empty(" ") is True, "Строка с пробелом должна возвращать True, согласно документации"
    assert utils.is_empty("Plants vs. Zombies") is False, "Непустая строка должна возвращать False"
    # Негативный тест
    # Проверка на None в качестве аргумента
    with pytest.raises(TypeError):
        utils.is_empty(None)

def test_list_to_string():
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Superman", "Batman"]) == "Superman, Batman"
    assert utils.list_to_string(["Chilly", "Willy"], "-") == "Chilly-Willy"
    # Негативный тест: передаем не список
    with pytest.raises(TypeError):
        utils.list_to_string(None)