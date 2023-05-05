from src.item import Item


class MixinLanguage:
    __slots__ = ["EN", "RU"]
    language = "EN"

    def change_lang(self):
        if MixinLanguage.language == "EN":
            MixinLanguage.language = "RU"
        else:
            MixinLanguage.language = "EN"

        return self


class Keyboard(Item, MixinLanguage):
    def __init__(self, item_name, price, quantity):
        super().__init__(item_name, price, quantity)
