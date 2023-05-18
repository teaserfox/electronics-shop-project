"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


@pytest.mark.parametrize('item1, rez', [(Item('item1', 10000, 20), 10000 * 20),
                                        (Item('item2', 20000, 5), 20000 * 5)])
def test_calculate_total_price(item1, rez):
    assert item1.calculate_total_price() == rez


@pytest.fixture
def item1():
    return Item('Смартфон', 10000, 20)


@pytest.fixture
def Item():
    return Item('Смартфон', 10000, 20)


def test_repr(item):
    assert item.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_init(item1):
    """Тестирует метод init."""
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


# def test_instantiate_from_csv(item1):
# """Тестирует метод instantiate_from_csv."""
# Item.instantiate_from_csv(CSV_FILE='items.csv')
# assert len(Item.all[0].name) == 5
# assert Item.all[0].name == 'Смартфон'


def test_apply_discount(item1):
    """Тестирует метод apply_discount."""
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_len_name_setter(item1):
    """Тестирует сеттер  self.__name."""
    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'


def test_change_name_setter(item1):
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_string_to_number(item1):
    """Тестирует метод string_to_number."""
    assert item1.string_to_number("10000") == 10000
    assert item1.string_to_number("2.034") == 2


def test_exception_instantiate_from_csv():
    Item.CSV_FILE = '123'
    with pytest.raises(FileNotFoundError) as ex:
        Item.instantiate_from_csv()
    assert str(ex.value) == f'Отсутствует файл {Item.CSV_FILE}'

    Item.CSV_FILE = 'items_test.csv'
    with pytest.raises(InstantiateCSVError) as ex:
        Item.instantiate_from_csv()
    assert str(ex.value) == f'Файл {Item.CSV_FILE} поврежден'
