"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def smartphone():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def laptop():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(smartphone, laptop):
    assert smartphone.calculate_total_price() == 200000
    assert laptop.calculate_total_price() == 100000


def test_price(smartphone, laptop):
    assert smartphone.price == 10000
    assert laptop.price == 20000


def test_change_name(smartphone):
    smartphone.name = 'Smartphone'
    assert smartphone.name == 'Smartphone'
    smartphone.name = 'Chuka'
    assert smartphone.name == 'Chuka'


def test_name_length(smartphone):
    smartphone.name = 'Obemetvoudochku'
    assert 'Длина наименования товара превышает 10 символов.'


def test_item_all(smartphone):
    smartphone.instantiate_from_csv()
    assert len(smartphone.all) == 12
    item1 = smartphone.all[1]
    assert smartphone.name == 'Смартфон'


def test_string_to_number(smartphone):
    assert smartphone.string_to_number('5') == 5
    assert smartphone.string_to_number('5.0') == 5
    assert smartphone.string_to_number('5.5') == 5


def test_magic_methods(smartphone):
    assert repr(smartphone) == "Item('Смартфон', 10000, 20)"
    assert str(smartphone) == 'Смартфон'
    smartphone.name = 'Buba'
    smartphone.price = 228
    smartphone.quantity = 0
    assert repr(smartphone) == "Item('Buba', 228, 0)"
    assert str(smartphone) == 'Buba'


def test_add(smartphone, phone):

    assert smartphone + phone == 25
    assert phone + phone == 10


def test_repr_and_str(phone):
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


