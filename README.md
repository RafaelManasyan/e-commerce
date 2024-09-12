# E-commerce project
## Modules
The project consists of two modules: main.py and product_category.py, and tests for them with fixtures
## How it works?
Product and category classes are created by specified parameters when calling the function
```chatinput
product1 = Product(
        "Samsung Galaxy S23 Ultra", 
        "256GB, Серый цвет, 200MP камера", 
        180000.0, 
        5
    )
```

## How to get product information?
First of all, you should initialise Product class object and then print it
```chatinput
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
print(product1)
```