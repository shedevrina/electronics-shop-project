"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.class_product import Item

@pytest.fixture

def class_product1():
    pay_rate = 0.8
    return Item("Смартфон", 10000, 20)

def test_item_calculate_total_price(class_product1):
    assert class_product1.calculate_total_price() == 200000

def test_item_apply_discount(class_product1):
    assert 10000*class_product1.pay_rate == class_product1.price
