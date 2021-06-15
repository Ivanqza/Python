orders = int(input())
total = 0

while not orders == 0:
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    price_for_coffee = price_per_capsule * days * capsules
    total += price_for_coffee
    orders -= 1
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")


print(f"Total: ${total:.2f}")