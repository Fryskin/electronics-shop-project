from src.item import Item
if __name__ == '__main__':
    # Файл items_broken.csv отсутствует.
    Item.instantiate_from_csv('')
    # FileNotFoundError: Отсутствует файл items.csv

    # В файле items_broken.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
