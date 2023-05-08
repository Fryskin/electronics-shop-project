from src.item import Item


class MixinLanguage:
    __slots__ = ["EN", "RU"]

    language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"

        return self


class Keyboard(Item, MixinLanguage):
    def __init__(self, item_name, price, quantity):
        super().__init__(item_name, price, quantity)
