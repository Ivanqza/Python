import sys

count_of_numbers = int(input())
odd_sum = 0
odd_max_number = - sys.maxsize
odd_min_number = sys.maxsize
even_sum = 0
even_max_number = - sys.maxsize
even_min_number = sys.maxsize

for numbers in range(1, count_of_numbers + 1):
    number = float(input())
    if numbers %2 == 0:
        even_sum += number
        if number > even_max_number:
            even_max_number = number
        if number < even_min_number:
            even_min_number = number
    else:
        odd_sum += number
        if number > odd_max_number:
            odd_max_number = number
        if number < odd_min_number:
            odd_min_number = number

print(f"OddSum={odd_sum:.2f},")
if odd_min_number == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min_number:.2f},")
if odd_max_number == - sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max_number:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min_number == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min_number:.2f},")
if even_max_number == - sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max_number:.2f}")
