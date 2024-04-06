# Создайте класс "Товар" с атрибутами "название" и "цена".
# Создайте объекты этого класса, представляющие разные товары, и выведите информацию о них.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Laptop(Product):
    def __init__(self, name, price):
        super().__init__(name, price)


class Mobile(Product):
    def __init__(self, name, price):
        super().__init__(name, price)


products = [
    Laptop("Dell XPS", 1500),
    Mobile("iPhone 12", 1000),
    Laptop("HP Spectre", 1200),
    Mobile("Samsung Galaxy S21", 800)
]


# Декоратор для вывода товаров с максимальной и минимальной ценой
def min_max_price_decorator(func):
    def wrapper(products):
        max_price_product = max(products, key=lambda x: x.price)
        min_price_product = min(products, key=lambda x: x.price)

        print("Товар с максимальной ценой:")
        print(f"Название: {max_price_product.name}, Цена: {max_price_product.price}")

        print("\nТовар с минимальной ценой:")
        print(f"Название: {min_price_product.name}, Цена: {min_price_product.price}")

        return func(products)

    return wrapper


@min_max_price_decorator
def print_products(products):
    for product in products:
        print(f"\nНазвание: {product.name}, Цена: {product.price}")


print_products(products)
