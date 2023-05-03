from src.item import Item


class Phone(Item):

    def __init__(self, item_name, price, quantity, number_of_sim: int):
        super().__init__(item_name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if issubclass(Phone, Item):
            return self.quantity + other.quantity

        else:
            return None



