numbers = input().split()
reverse = []

while numbers:
    reverse.append(numbers.pop())

print(f"{' '.join(reverse)}")
