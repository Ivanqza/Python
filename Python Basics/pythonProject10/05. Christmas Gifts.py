command = input()
gift_for_kids = 0
gift_for_adults = 0
price_of_gift_for_kids = 5
price_of_gift_for_adults = 15


while command != "Christmas":
    current_number = int(command)
    if current_number > 16:
        gift_for_adults += 1
    else:
        gift_for_kids += 1
    command = input()

total_price_of_gifts_for_kids = gift_for_kids * 5
total_price_of_gifts_for_adults = gift_for_adults * 15
print(f"Number of adults: {gift_for_adults}")
print(f"Number of kids: {gift_for_kids}")
print(f"Money for toys: {total_price_of_gifts_for_kids}")
print(f"Money for sweaters: {total_price_of_gifts_for_adults}")