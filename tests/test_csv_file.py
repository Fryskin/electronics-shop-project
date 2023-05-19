import csv

from src.item import Item, InstantiateCSVError
import pytest


def test_instantiate_from_csv_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("ite.csv")


def test_instantiate_from_csv_key_error():
    with pytest.raises(KeyError):
        Item.instantiate_from_csv("items.csv")








