hall_rent = int(input())
price_of_cake = hall_rent * 20 / 100
price_of_drinks = price_of_cake - price_of_cake * 45 / 100
animator_price = hall_rent / 3
total_sum = hall_rent + price_of_cake + price_of_drinks + animator_price
print(total_sum)