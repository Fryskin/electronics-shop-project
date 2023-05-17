import csv
import math


class InstantiateCSVError(Exception):
    def __init__(self):
        self.massage = 'Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, item_name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param item_name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = item_name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

        else:
            return None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, item_name):
        self.__name = item_name
        if len(item_name) >= 10:
            print('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return int(self.quantity * self.price)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name='items_broken.csv'):
        try:
            with open(file_name, newline='') as csr_file:
                try:
                    reader = csv.DictReader(csr_file)

                    for row in reader:

                        item_name = row['name']
                        price = row['price']
                        quantity = row['quantity']

                except KeyError:
                    print("Файл items_broken.csv поврежден")

                else:
                    cls(item_name, price, quantity)
                    csr_file.close()

        except FileNotFoundError:
            print("Отсутствует файл items_broken.csv")

    @staticmethod
    def string_to_number(number):

        return math.floor(float(number))
