n = int(input())
are_chairs_enough = True
free_chairs = 0

for room_number in range(1, n +1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    difference = abs(len(chairs) - n_people)
    if len(chairs) < n_people:
        print(f"{difference} more chairs needed in room {room_number}")
        are_chairs_enough = False
    else:
        free_chairs += difference

if are_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")


