total_days = int(input())
total_bakers = int(input())
total_cakes = int(input())
total_waffles = int(input())
total_pancakes = int(input())
price_of_cake = 45
price_of_waffle = 5.8
price_of_pancake = 3.2
total_cakes_per_day = total_cakes * price_of_cake
total_waffles_per_day = total_waffles * price_of_waffle
total_pancakes_per_day = total_pancakes * price_of_pancake
total_turnover_per_day = (total_cakes_per_day + total_waffles_per_day + total_pancakes_per_day) * total_bakers
total_sum = total_turnover_per_day * total_days
final_sum = total_sum - total_sum / 8
print(final_sum)
