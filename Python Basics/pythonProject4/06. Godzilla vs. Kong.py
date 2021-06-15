budget = float(input())
number_of_statists = int(input())
price_of_costume = float(input())
decor_price = budget * 0.1
costumes_price = number_of_statists * price_of_costume

if number_of_statists > 150:
    costumes_price *= 0.9  # 90% ot costumes_price ili (10% discount)

money_needed = decor_price + costumes_price
difference = abs(money_needed - budget)

if money_needed > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
