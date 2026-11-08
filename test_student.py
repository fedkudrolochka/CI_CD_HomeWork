
import pytest
from umnichka import ask_deadline


def test_success():
    assert ask_deadline(20, "да") == "Михаил: Работа сдана!"


def test_early():
    assert ask_deadline(15, "да") == "Михаил: Молодец!"


def test_move_deadline():
    assert ask_deadline(15, "нет") == "Михаил: Сместим!"


def test_wrong_number():
    with pytest.raises(ValueError, match="Неверное число"):
        ask_deadline(200, "да")


def test_deadline_passed():
    with pytest.raises(ValueError, match="Надо было думать раньше"):
        ask_deadline(21, "нет")


def test_no_homework_on_deadline():
    with pytest.raises(ValueError, match="Надо было думать раньше"):
        ask_deadline(20, "нет")


def test_wrong_answer():
    with pytest.raises(ValueError, match="Введите да или нет"):
        ask_deadline(15, "может быть")
