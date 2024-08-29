def test_init_product(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"


def test_init_cat(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.category_count == 1
    assert category_smartphones.product_count == 3
