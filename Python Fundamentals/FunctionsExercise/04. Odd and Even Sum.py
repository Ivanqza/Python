def get_odd_even_sum(num_as_string):
    odd_num = 0
    even_num = 0
    for char in num_as_string:
        current_char_as_num = int(char)
        if current_char_as_num % 2 == 0:
            even_num += current_char_as_num
        else:
            odd_num += current_char_as_num
    return [odd_num, even_num]


numbers_as_string = input()
result = get_odd_even_sum(numbers_as_string)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")