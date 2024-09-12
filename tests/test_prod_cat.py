import pytest


def test_init_product(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"


def test_init_cat(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.category_count == 1
    assert category_smartphones.product_count == 3


def test_adding_product(product_samsung, product_iphone):
    prod_sum = product_iphone + product_samsung
    assert prod_sum == 2580000.0


def test_str_product(product_samsung):
    prod_str = str(product_samsung)
    assert prod_str == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_prods(product_grass, product_smartphone):
    with pytest.raises(TypeError):
        assert product_grass + product_smartphone == TypeError


def test_check_prod_before_adding(category_smartphones):
    with pytest.raises(TypeError):
        assert category_smartphones.add_product("smartphone3") == TypeError
