target_steps = 10000
current_steps = 0
going_home = False

while current_steps < target_steps:
    command = input()
    if command == "Going home":
        going_home = True
        break
    steps = int(command)
    current_steps += steps

if going_home:
    steps = int(input())
    current_steps += steps

difference = abs(current_steps - target_steps)
if current_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")