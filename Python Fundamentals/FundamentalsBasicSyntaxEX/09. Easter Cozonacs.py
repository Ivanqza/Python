budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price_box = flour_price * 1.25
milk_price_250 = milk_price_box / 4
cozonac_price = flour_price + eggs_price + milk_price_250
counter = 0
colored_eggs = 0


while budget - cozonac_price >= 0:
    colored_eggs += 3
    counter += 1
    if counter % 3 == 0:
        colored_eggs -= counter - 2
    budget -= cozonac_price

print(f"You made {counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")