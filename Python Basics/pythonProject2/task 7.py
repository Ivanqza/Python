price_of_strawberries = float(input())
total_bananas = float(input())
total_oranges = float(input())
total_raspberries = float(input())
total_strawberries = float(input())
price_of_raspberries = price_of_strawberries / 2
price_of_oranges = price_of_raspberries - (price_of_raspberries * 0.4)
price_of_bananas = price_of_raspberries - (price_of_raspberries * 0.8)
total_sum_of_raspberries = total_raspberries * price_of_raspberries
total_sum_of_oranges = total_oranges * price_of_oranges
total_sum_of_bananas = total_bananas * price_of_bananas
total_sum_of_strawberries = total_strawberries * price_of_strawberries
total_sum = total_sum_of_raspberries + total_sum_of_strawberries + total_sum_of_bananas + total_sum_of_oranges
print(total_sum)

