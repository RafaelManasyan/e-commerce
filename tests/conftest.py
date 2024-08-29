import pytest
from src.product_category import *


@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_smartphones():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )
