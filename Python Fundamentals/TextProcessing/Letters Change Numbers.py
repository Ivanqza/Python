# capital_letters = 65 - 90
# not_capital_letters = 97 - 122

data = [el.strip() for el in input().split()]
searched_number = ""
current_letters = []
to_divide_or_multiply_by = 0
to_subtract_or_add_by = 0
number = 0
for_each_sum = []

for word in range(len(data)):
    for el in data[word]:
        if el.isnumeric():
            searched_number += el
        else:
            current_letters.append(el)

    if 65 <= ord(current_letters[0]) <= 90:
        to_divide_or_multiply_by = ord(current_letters[0]) - 64
        number += int(searched_number) / to_divide_or_multiply_by
    elif 97 <= ord(current_letters[0]) <= 122:
        to_divide_or_multiply_by = ord(current_letters[0]) - 96
        number += int(searched_number) * to_divide_or_multiply_by

    if 65 <= ord(current_letters[1]) <= 90:
        to_subtract_or_add_by = ord(current_letters[1]) - 64
        number -= to_subtract_or_add_by
    elif 97 <= ord(current_letters[1]) <= 122:
        to_subtract_or_add_by = ord(current_letters[1]) - 96
        number += to_subtract_or_add_by

    for_each_sum.append(number)
    number = 0
    searched_number = ""
    current_letters = []

print(f"{sum(for_each_sum):.2f}")