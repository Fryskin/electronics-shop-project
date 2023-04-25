import csv
import math


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
        self.__name = item_name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

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
    def instantiate_from_csv(cls):
        with open('items.csv', newline='') as csr_file:
            reader = csv.DictReader(csr_file)

            for row in reader:

                item_name = row['name']
                price = row['price']
                quantity = row['quantity']

                cls(item_name, price, quantity)

            csr_file.close()

    @staticmethod
    def string_to_number(number):

        return math.floor(float(number))
