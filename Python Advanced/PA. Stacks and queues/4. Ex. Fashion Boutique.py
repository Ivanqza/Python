box = []

for piece in input().split():
    box.append(int(piece))
rack_counter = 1
current_rack_weight = 0
rack_capacity = int(input())

for item in range(len(box)):
    current_piece = box.pop()
    if current_piece + current_rack_weight > rack_capacity:
        rack_counter += 1
        current_rack_weight = 0
    current_rack_weight += current_piece

print(rack_counter)
