number_of_cats = int(input())
first_group = 0
second_group = 0
third_group = 0
price_of_food_per_kg = 12.45
total_grams_of_food = 0
for cats in range(number_of_cats):
    cat_food_eaten = float(input())
    if 100 <= cat_food_eaten < 200:
        first_group += 1
        total_grams_of_food += cat_food_eaten
    elif 200 <= cat_food_eaten < 300:
        second_group += 1
        total_grams_of_food += cat_food_eaten
    elif 300 <= cat_food_eaten < 400:
        third_group += 1
        total_grams_of_food += cat_food_eaten

total_price_of_food = (total_grams_of_food / 1000) * price_of_food_per_kg

print(f"Group 1: {first_group} cats.")
print(f"Group 2: {second_group} cats.")
print(f"Group 3: {third_group} cats.")
print(f"Price for food per day: {total_price_of_food:.2f} lv.")