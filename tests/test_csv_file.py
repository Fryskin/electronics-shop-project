from src.item import Item
import pytest


@pytest.fixture
def true_file():
    return "true_file.csv"


@pytest.fixture
def file_not_exist():
    return "file_not_exist.csv"


@pytest.fixture
def broken_file():
    return "broken_file.csv"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("")
    assert 'Отсутствует файл items_broken.csv'

    Item.instantiate_from_csv("items_broken.csv")
    assert "Файл items_broken.csv поврежден"



