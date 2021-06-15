import math
gender = input()
weight = float(input())
height = float(input())
age = int(input())
activity_level = input()
height_in_cm = height * 100

if gender == "m":
    metabolism = 66 + (13.7 * weight) + (5 * height_in_cm) - (6.8 * age)
else:
    metabolism = 655 + (9.6 * weight) + (1.8 * height_in_cm) - (4.7 * age)

if activity_level == "sedentary":
    metabolism *= 1.2
if activity_level == "lightly active":
    metabolism *= 1.375
if activity_level == "moderately active":
    metabolism *= 1.55
if activity_level == "very active":
    metabolism *= 1.725

print(f"To maintain your current weight you will need {math.ceil(metabolism)} calories per day.")