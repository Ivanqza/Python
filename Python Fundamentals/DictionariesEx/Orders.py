data = input()
products = {}

# product_prices = {}
# product_quatities = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

    data = input()

for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")

#     if name not in product_prices:
#         product_prices[name] = price
#         product_quatities[name] = quantity
#     else:
#         product_prices[name] = price
#         product_quatities[name] += quantity
#
#     data = input()
#
# for product, price in product_prices.items():
#     result = price * product_quatities[product]
#     print(f"{product} -> {result:.2f}")