import csv

from src.item import Item, InstantiateCSVError
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


def test_instantiate_from_csv_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        try:
            with open('', newline='') as csr_file:
                try:
                    reader = csv.DictReader(csr_file)

                    for row in reader:
                        item_name = row['name']
                        price = row['price']
                        quantity = row['quantity']

                except KeyError:
                    raise KeyError

                else:
                    attributes = (item_name, price, quantity)
                    csr_file.close()

        except FileNotFoundError:
            raise FileNotFoundError


def test_instantiate_from_csv_key_error():
    with pytest.raises(KeyError):
        try:
            with open('items_broken.csv', newline='') as csr_file:
                try:
                    reader = csv.DictReader(csr_file)

                    for row in reader:
                        item_name = row['name']
                        price = row['price']
                        quantity = row['quantity']

                except KeyError:
                    raise KeyError

                else:
                    attributes = (item_name, price, quantity)
                    csr_file.close()

        except FileNotFoundError:
            raise FileNotFoundError






