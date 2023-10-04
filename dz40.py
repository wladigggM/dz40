def buy_product(*args: tuple):
    products = {}
    for product in args:
        name, price = product
        products[name] = price
    return products


print(buy_product(('Кружка', 300), ('Стакан', 400), ('кофе 500 гр', 800)))
