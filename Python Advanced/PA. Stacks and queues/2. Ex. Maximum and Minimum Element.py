n = int(input())
stack = []

for index in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()
    elif command[0] == '3':
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == '4':
        if len(stack) > 0:
            print(min(stack))

reverse = []
while stack:
    reverse.append(str(stack.pop()))

print(f"{', '.join(reverse)}")