start = int(input())
end = int(input())
magic_number = int(input())
combinations = 0
magic_number_found = False

for x in range (start,end+1):
    for y in range (start, end+1):
        combinations += 1
        sum = x + y
        if sum == magic_number:
            print(f"Combination N:{combinations} ({x} + {y} = {magic_number})")
            magic_number_found = True
            break
    if magic_number_found:
            break
if not magic_number_found:
    print(f"{combinations} combinations - neither equals {magic_number}")