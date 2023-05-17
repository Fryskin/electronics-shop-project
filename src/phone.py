from src.item import Item


class NumberOfSimError(Exception):
    def __init__(self, value):
        self.massage = "Количество физических SIM-карт должно быть целым числом больше нуля."


class Phone(Item):

    def __init__(self, item_name, price, quantity, number_of_sim: int):
        super().__init__(item_name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        try:
            if value <= 0:
                raise ValueError

        except ValueError:
            print("Количество физических SIM-карт должно быть целым числом больше нуля.")

        else:
            self._number_of_sim = value
