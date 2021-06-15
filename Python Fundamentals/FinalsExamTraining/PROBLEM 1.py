message = input()

sum = 0
data = input()
while not data == "Finish":
    command = data.split()
    if command[0] == "Replace":
        current_char, new_char = command[1], command[2]
        if current_char in message:
            message = message.replace(current_char, new_char)
            print(message)
    elif command[0] == "Cut":
        start = int(command[1])
        end = int(command[2])
        if 0 <= start and end <= len(message):
            edit = message[start:end+1]
            message = message.replace(edit, "", 1)
            print(message)
        else:
            print(f"Invalid indices!")
    elif command[0] == "Make":
        if command[1] == "Upper":
            message = message.upper()
            print(message)
        elif command[1] == "Lower":
            message = message.lower()
            print(message)
    elif command[0] == "Check":
        if command[1] in message:
            print(f"Message contains {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")
    elif command[0] == "Sum":
        start = int(command[1])
        end = int(command[2])
        if 0 <= start and end <= len(message):
            for char in message[start:end+1]:
                sum += ord(char)
            print(sum)
        else:
            print(f"Invalid indices!")
    data = input()



