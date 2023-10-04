def buy_product(*args: tuple):
    products = {}
    for product in args:
        name, price = product
        products[name] = price
    return products


basket = buy_product(('Кружка', 300), ('Стакан', 400), ('кофе 500 гр', 800))
print(f"Корзина: {basket}")


def total_prod_pirce(basket: dict):
    total_price = 0
    for product in basket.values():
        total_price += product
    return total_price


print(f"Стоймость товаров: {total_prod_pirce(basket)}")
