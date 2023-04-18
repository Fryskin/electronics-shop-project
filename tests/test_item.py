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
