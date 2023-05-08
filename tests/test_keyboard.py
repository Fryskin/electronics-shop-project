from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard(keyboard):
    assert str(keyboard) == "Dark Project KD87A"

    assert str(keyboard.language) == "EN"

    keyboard.change_lang()
    assert str(keyboard.language) == "RU"

    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"

    keyboard.language = 'CH'
    assert AttributeError
