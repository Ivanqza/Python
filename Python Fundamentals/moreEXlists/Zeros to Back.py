numbers = input().split(", ")

for num in numbers:
    if num == "0":
        numbers.remove("0")
        numbers.append("0")

numbers = [int(index) for index in numbers]
print(numbers)