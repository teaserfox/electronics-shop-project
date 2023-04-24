"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.mark.parametrize('item1, rez', [(Item('item1', 10000, 20), 10000 * 20),
                                        (Item('item2', 20000, 5), 20000 * 5)])

def test_calculate_total_price(item1, rez):
    assert item1.calculate_total_price() == rez








