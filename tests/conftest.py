import pytest
from src.product_category import *


@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_samsung():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,"S23 Ultra", 256, "Серый")


@pytest.fixture
def category_smartphones():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )


@pytest.fixture
def category_empty():
    return Category("Пустая категория", "Категория без продуктов", [])
