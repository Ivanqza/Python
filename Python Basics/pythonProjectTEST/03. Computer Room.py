month = input()
hours_spent = int(input())
number_of_friends = int(input())
day_or_night = input()
cost_of_visit = 0
price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price_per_hour = 10.50
        if number_of_friends >= 4:
            price_per_hour *= 0.9
            if hours_spent >= 5:
                price_per_hour *= 0.5
    else:
        price_per_hour = 8.40
        if number_of_friends >= 4:
            price_per_hour *= 0.9
            if hours_spent >= 5:
                price_per_hour *= 0.5
elif month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        price_per_hour = 12.60
        if number_of_friends >= 4:
            price_per_hour *= 0.9
            if hours_spent >= 5:
                price_per_hour *= 0.5
    else:
        price_per_hour = 10.20
        if number_of_friends >= 4:
            price_per_hour *= 0.9
            if hours_spent >= 5:
                price_per_hour *= 0.5

cost_of_visit = (price_per_hour * number_of_friends) * hours_spent
print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {cost_of_visit:.2f}")

