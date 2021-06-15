points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points += 5  # bonus_points = bonus_points + 5
elif points > 1000:
    bonus_points += points * 0.1  # points * 10/100  --> 10% from points
else:
    bonus_points += points * 0.2

if points % 2 == 0:      #проверка дали е четно
    bonus_points += 1

if points % 10 == 5:     #проверка дали завършва на 5
    bonus_points += 2

print(bonus_points)
print(bonus_points + points)
