import sys

min_number = sys.maxsize
command = input()

while command != "Stop":
    current_number = int(command)
    if current_number < min_number:
        min_number = current_number
    command = input()
if min_number != - sys.maxsize:
    print(min_number)