holiday_price = float(input())
np = int(input())
nd = int(input())
nt = int(input())
nm = int(input())
ntr = int(input())

Puzzle_price = 2.60
Doll_price = 3
Teddy_bear_price = 4.10
Minion_price = 8.20
Truck_price = 2

earnings = np * Puzzle_price + nd * Doll_price + nt * Teddy_bear_price + nm * Minion_price + ntr * Truck_price
number_of_items = np + nd + nt + nm + ntr

if number_of_items >= 50:
    Discount = earnings * 0.25
    Final_price = earnings - Discount
else:
    Final_price = earnings

rent = Final_price * 0.1

net_earnings = Final_price - rent

money_left = net_earnings - holiday_price

if net_earnings >= holiday_price:
    print(f"Yes! {money_left:.2f} lv left.")
elif net_earnings < holiday_price:
    not_enough = holiday_price - net_earnings
    print(f"Not enough money! {not_enough:.2f} lv needed.")
