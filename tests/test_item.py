"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def smartphone():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def laptop():
    return Item("Ноутбук", 20000, 5)


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
    assert len(smartphone.all) == 6
    item1 = smartphone.all[1]
    assert smartphone.name == 'Смартфон'


def test_string_to_number(smartphone):
    assert smartphone.string_to_number('5') == 5
    assert smartphone.string_to_number('5.0') == 5
    assert smartphone.string_to_number('5.5') == 5
