money = float(input())
final_year = int(input())
years_old = 18

for year in range(1800, final_year+1):
    if year %2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * years_old
    years_old += 1
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")