import sys

count_of_numbers = int(input())
max_number = - sys.maxsize
sum_of_numbers = 0

for numbers in range(1, count_of_numbers +1):
    number = int(input())
    sum_of_numbers += number
    if number > max_number:
        max_number = number
if max_number == sum_of_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_of_numbers - max_number))
    print("No")
    print(f"Diff = {difference}")
