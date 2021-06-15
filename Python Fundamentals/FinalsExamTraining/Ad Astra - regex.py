import re
text = input()
total_calories = 0
pattern = r"(#|\|)(?P<product>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|1000))\1"

matches = re.finditer(pattern, text)
food_data = []

for match in matches:
    object_dict = match.groupdict()
    food_data.append(object_dict)
    total_calories += int(object_dict['calories'])

day = total_calories // 2000

print(f"You have food to last you for: {day} days!")
for food in food_data:
    print(f"Item: {food['product']}, Best before: {food['date']}, Nutrition: {food['calories']}")