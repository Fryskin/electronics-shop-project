from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    print(Item.all)
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    print(Item.all)
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    print(Item.all)
    assert len(Item.all) == 6  # в файле 5 записей с данными по товарам, но 1 - я инициализировал выше, поэтому их 6

    item1 = Item.all[1]    # так как [0] - это элемент из 4 строки, то нужный элемент - [1]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
