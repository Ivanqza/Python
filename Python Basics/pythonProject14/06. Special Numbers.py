number = int(input())
for numbers in range(1111, 10000):
    is_magic = True
    number_as_string = str(numbers)
    for digit in number_as_string:
        if int(digit) == 0 or number % int(digit) != 0:
            is_magic = False
            break
    if is_magic:
        print(f"{number_as_string}", end=" ")