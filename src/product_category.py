from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class InfoMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'


class Product(BaseProduct, InfoMixin):
    """Product creating class"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    @classmethod
    def new_product(cls, product_dict):
        new_prod = cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )
        return new_prod

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __repr__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        else:
            return (self.__price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):

    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Category creating class"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def middle_price(self):
        try:
            avg_price_of_prod = list(product.price for product in self.__products)
            middle_price = round(sum(avg_price_of_prod) / len(avg_price_of_prod), 2)
            return middle_price
        except ZeroDivisionError:
            return 'Category have no products'

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError

    @property
    def products(self):
        prod_str = ""
        for product in self.__products:
            prod_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return prod_str

    def __str__(self):
        prod_count = 0
        for product in self.__products:
            prod_count += product.quantity
        return f'{self.name}, количество продуктов: {prod_count} шт.'
