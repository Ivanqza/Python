cake_lenght = int(input())
cake_width = int(input())
max_slices = cake_width * cake_lenght
slices_taken = 0

while slices_taken < max_slices:
    command = input()
    if command == "STOP":
        break
    slices = int(command)
    slices_taken += slices

difference = abs(max_slices - slices_taken)

if slices_taken < max_slices:
    print(f"{difference} pieces are left.")
else:
    print(f"No more cake left! You need {difference} pieces more.")